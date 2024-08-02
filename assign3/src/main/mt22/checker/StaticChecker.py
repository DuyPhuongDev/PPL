from AST import *
from Visitor import Visitor
from StaticError import *
from Utils import *
from abc import ABC
from functools import reduce

class Symbol: pass
class VarSymbol(Symbol):
    def __init__(self, name: str, typ: Type):
        self.name = name
        self.typ = typ

class ParamSymbol(Symbol):
    def __init__(self,name: str, typ: Type, inherit: bool = False, out: bool = False ) -> None:
        self.name = name
        self.typ = typ
        self.inherit = inherit
        self.out = out
        
class FuncSymbol(Symbol):
    def __init__(self,name: str, params: List[ParamSymbol], returnTyp: Type, inherit: str or None) -> None:
        self.name = name
        self.params = params
        self.typ = returnTyp
        self.inherit = inherit

class GlobalFunc(Symbol):
    def __init__(self, name: str, param: List[ParamSymbol], returnTyp: Type) -> None:
        self.name = name
        self.params = param
        self.typ = returnTyp

class GetPrototype(Visitor):
    def __init__(self, ast) -> None:
        self.ast = ast
    def visitProgram(self, ast, param):
        env = []
        for decl in ast.decls:
            self.visit(decl, env)
        return env
    
    def visitVarDecl(self, ast, param):
        param += [VarSymbol(ast.name, ast.typ)]
    
    def visitFuncDecl(self, ast, param):
        params = reduce(lambda prev, curr: self.visit(curr, prev), ast.params, [])
        param += [FuncSymbol(ast.name, params , ast.return_type, ast.inherit)]
    
    def visitParamDecl(self, ast, param):
        param += [ParamSymbol(ast.name, ast.typ, ast.inherit, ast.out)]
        return param
     
class InferType():
    @staticmethod
    def infer(name, typ, param):
        for env in param:
            found = Utils().lookup(name, env,lambda x: x.name)
            if found:
                found.typ = typ
                return typ
               
class StaticChecker(Visitor):
    
    def check(self):
        return self.visitProgram(self.ast, [])

    def __init__(self, ast):
        self.ast = ast
        self.env = [[
            GlobalFunc("readInteger", [], IntegerType()),
            GlobalFunc("printInteger", [ParamSymbol("", IntegerType())], VoidType()),
            GlobalFunc("readFloat", [], FloatType()),
            GlobalFunc("writeFloat", [ParamSymbol("", FloatType())], VoidType()),
            GlobalFunc("readBoolean", [], BooleanType()),
            GlobalFunc("printboolean", [ParamSymbol("", BooleanType())], VoidType()),
            GlobalFunc("readString", [], StringType()),
            GlobalFunc("printString", [ParamSymbol("", StringType())], VoidType()),
            GlobalFunc("super", [], VoidType()),
            GlobalFunc("preventDefault", [], VoidType())
        ]]
        self.curr_var = None #luu bien hien tai dang visit
        self.prototype = [] # luu moi truong so bo cua chuong trinh
        self.curr_func = None # luu name cua function hien tai dang duoc vieng tham
        self.inloop = []
        self.returned = False
        self.curr_arr = None
        self.arrflag = False
        self.typeinfer = None
    
    # type
    def visitIntegerType(self, ast, param): return IntegerType()
    def visitFloatType(self, ast, param): return FloatType()
    def visitBooleanType(self, ast, param): return BooleanType()
    def visitStringType(self, ast, param): return StringType()
    def visitArrayType(self, ast, param): return ArrayType(ast.dimensions, ast.typ)
    def visitAutoType(self, ast, param): return AutoType()
    def visitVoidType(self, ast, param): return VoidType()

    ######  Expr  #####
    def visitBinExpr(self, ast, param):
        #print('visit bin')
        ltype = self.visit(ast.left, param)
        rtype = self.visit(ast.right, param)
        #print(ltype, '-', rtype)
        if type(ltype) is AutoType:
            if not self.typeinfer and type(rtype) is AutoType: return AutoType()
            elif type(rtype) is not AutoType: ltype = InferType.infer(ast.left.name,rtype,param)
        else:
            if type(rtype) is AutoType: rtype = InferType.infer(ast.right.name, ltype, param)
        if ast.op in ['-', '+', '*', '/']: 
            #print(ltype, rtype)
            #print(type(ltype) is AutoType and type(rtype) is AutoType)
            if type(ltype) is AutoType and type(rtype) is AutoType:
                if type(self.typeinfer) not in [IntegerType, FloatType]: return None
                #print(type(ast.left), '-', type(ast.right))
                if type(ast.left) is Id:
                    ltype =  InferType.infer(ast.left.name, self.typeinfer, param)
                else:
                    found = Utils().lookup(ast.left.name, self.prototype, lambda x: x.name)
                    if not found: raise Undeclared(Function(), ast.left.name)
                    found.typ = self.typeinfer
                if type(ast.right) is Id:
                    rtype = InferType.infer(ast.right.name, self.typeinfer, param)
                else:
                    found = Utils().lookup(ast.right.name, self.prototype, lambda x: x.name)
                    if not found: raise Undeclared(Function(), ast.right.name)
                    found.typ = self.typeinfer
                return self.typeinfer
            if type(ltype) is IntegerType and type(rtype) is IntegerType:
                return IntegerType() if ast.op != '/' else FloatType()
            if (type(ltype),type(rtype)) in [(IntegerType, FloatType), (FloatType, IntegerType), (FloatType, FloatType)]:
                return FloatType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op == '%': 
            if type(ltype) is AutoType and type(rtype) is AutoType:
                #print(type(ast.left), '-', type(ast.right))
                if type(self.typeinfer) is not IntegerType: return None
                if type(ast.left) is Id:
                    ltype =  InferType.infer(ast.left.name, self.typeinfer, param)
                else:
                    found = Utils().lookup(ast.left.name, self.prototype, lambda x: x.name)
                    if not found: raise Undeclared(Function(), ast.left.name)
                    found.typ = self.typeinfer
                if type(ast.right) is Id:
                    rtype = InferType.infer(ast.right.name, self.typeinfer, param)
                else:
                    found = Utils().lookup(ast.right.name, self.prototype, lambda x: x.name)
                    if not found: raise Undeclared(Function(), ast.right.name)
                    found.typ = self.typeinfer
                return self.typeinfer
            if type(ltype) is IntegerType and type(rtype) is IntegerType:
                return IntegerType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ['&&', '||']:
            if type(ltype) is AutoType and type(rtype) is AutoType:
                #print(type(ast.left), '-', type(ast.right))
                if type(self.typeinfer) is not BooleanType: return None
                if type(ast.left) is Id:
                    ltype =  InferType.infer(ast.left.name, self.typeinfer, param)
                else:
                    found = Utils().lookup(ast.left.name, self.prototype, lambda x: x.name)
                    if not found: raise Undeclared(Function(), ast.left.name)
                    found.typ = self.typeinfer
                if type(ast.right) is Id:
                    rtype = InferType.infer(ast.right.name, self.typeinfer, param)
                else:
                    found = Utils().lookup(ast.right.name, self.prototype, lambda x: x.name)
                    if not found: raise Undeclared(Function(), ast.right.name)
                    found.typ = self.typeinfer
                return self.typeinfer
            if type(ltype) is BooleanType and type(rtype) is BooleanType:
                return BooleanType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op == '::':
            if type(ltype) is AutoType and type(rtype) is AutoType:
                #print(type(ast.left), '-', type(ast.right))
                if type(self.typeinfer) is not StringType: return None
                if type(ast.left) is Id:
                    ltype =  InferType.infer(ast.left.name, self.typeinfer, param)
                else:
                    found = Utils().lookup(ast.left.name, self.prototype, lambda x: x.name)
                    if not found: raise Undeclared(Function(), ast.left.name)
                    found.typ = self.typeinfer
                if type(ast.right) is Id:
                    rtype = InferType.infer(ast.right.name, self.typeinfer, param)
                else:
                    found = Utils().lookup(ast.right.name, self.prototype, lambda x: x.name)
                    if not found: raise Undeclared(Function(), ast.right.name)
                    found.typ = self.typeinfer
                return self.typeinfer
            if type(ltype) is StringType and type(rtype) is StringType:
                return StringType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ['==', '!=']:
            if type(ltype) is AutoType and type(rtype) is AutoType:
                #print(type(ast.left), '-', type(ast.right))
                if type(self.typeinfer) not in [IntegerType, BooleanType]: return None
                if type(ast.left) is Id:
                    ltype =  InferType.infer(ast.left.name, self.typeinfer, param)
                else:
                    found = Utils().lookup(ast.left.name, self.prototype, lambda x: x.name)
                    if not found: raise Undeclared(Function(), ast.left.name)
                    found.typ = self.typeinfer
                if type(ast.right) is Id:
                    rtype = InferType.infer(ast.right.name, self.typeinfer, param)
                else:
                    found = Utils().lookup(ast.right.name, self.prototype, lambda x: x.name)
                    if not found: raise Undeclared(Function(), ast.right.name)
                    found.typ = self.typeinfer
                return self.typeinfer
            if (type(ltype), type(rtype)) in [(IntegerType, IntegerType), (IntegerType, BooleanType), (BooleanType, IntegerType), (BooleanType, BooleanType)]:
                return BooleanType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ['<', '>', '<=', '>=']:
            if type(ltype) is AutoType and type(rtype) is AutoType:
                #print(type(ast.left), '-', type(ast.right))
                if type(self.typeinfer) not in [IntegerType, FloatType]: return None
                if type(ast.left) is Id:
                    ltype =  InferType.infer(ast.left.name, self.typeinfer, param)
                else:
                    found = Utils().lookup(ast.left.name, self.prototype, lambda x: x.name)
                    if not found: raise Undeclared(Function(), ast.left.name)
                    found.typ = self.typeinfer
                if type(ast.right) is Id:
                    rtype = InferType.infer(ast.right.name, self.typeinfer, param)
                else:
                    found = Utils().lookup(ast.right.name, self.prototype, lambda x: x.name)
                    if not found: raise Undeclared(Function(), ast.right.name)
                    found.typ = self.typeinfer
                return self.typeinfer
            if (type(ltype), type(rtype)) in [(IntegerType, IntegerType), (IntegerType, FloatType), (FloatType, IntegerType), (FloatType,FloatType)]:
                return BooleanType()
            raise TypeMismatchInExpression(ast)
            
    def visitUnExpr(self, ast, param):
        etype = self.visit(ast.val, param)
        if not self.typeinfer and type(etype) is AutoType: return AutoType()
        
        if ast.op == '-':
            if type(etype) is AutoType:
                if type(self.typeinfer) not in [IntegerType, FloatType]: return None
                if type(ast.val) is Id:
                    etype =  InferType.infer(ast.val.name, self.typeinfer, param)
                else:
                    found = Utils().lookup(ast.val.name, self.prototype, lambda x: x.name)
                    if not found: raise Undeclared(Function(), ast.left.name)
                    found.typ = self.typeinfer
                return self.typeinfer
            if type(etype) in [IntegerType, FloatType]:
                return etype
            raise TypeMismatchInExpression(ast)
        if ast.op == '!':
            if type(etype) is AutoType:
                #if type(self.typeinfer) is not BooleanType: return None
                if type(ast.val) is Id:
                    etype =  InferType.infer(ast.val.name, BooleanType(), param)
                else:
                    found = Utils().lookup(ast.val.name, self.prototype, lambda x: x.name)
                    if not found: raise Undeclared(Function(), ast.left.name)
                    found.typ = BooleanType()
                return BooleanType()
            if type(etype) is BooleanType:
                return BooleanType()
            raise TypeMismatchInExpression(ast)
        
    def visitId(self, ast, param):
        # return type of id if not found => undeclared
        """ bien dang khai bao kh dc sd x: integer = x + 3; => error """
        #print('visit Id')
        ##print([list(map(lambda x: (x.name, type(x)), i)) for i in param])
        if self.curr_var is not None and self.curr_var == ast.name:
            raise Undeclared(Identifier(), ast.name)
        found = None
        for env in param:
            sym = Utils().lookup(ast.name, env, lambda x: x.name)
            if sym is not None and type(sym) in [VarSymbol, ParamSymbol]:
                found = sym
                break
        if found is None:
            raise Undeclared(Identifier(), ast.name)
        return found.typ
        
    def visitArrayCell(self, ast, param): 
        #print("visit arraycell")
        found = None
        for env in param:
            found = Utils().lookup(ast.name, env, lambda x: x.name)
            if found: break
        if not found: raise Undeclared(Identifier(), ast.name)
        if type(found.typ) is not ArrayType: raise TypeMismatchInExpression(ast)
        # dimension must be integer
        #dimentyps = [self.visit(x, param) for x in ast.cell]
        dimentyps = ast.cell
        for dimen in dimentyps:
            typ = self.visit(dimen, param)
            if type(typ) is not IntegerType: raise TypeMismatchInExpression(ast)
        if len(found.typ.dimensions)<len(dimentyps): raise TypeMismatchInExpression(ast)
        if len(found.typ.dimensions)>len(dimentyps): 
            newdimen = found.typ.dimensions[len(dimentyps):]
            return ArrayType(newdimen, found.typ.typ)
            
        return found.typ.typ
            
    def visitIntegerLit(self, ast, param): return IntegerType()
    def visitFloatLit(self, ast, param): return FloatType()
    def visitStringLit(self, ast, param): return StringType()
    def visitBooleanLit(self, ast, param): return BooleanType()
    
    def visitArrayLit(self, ast, param):
        #print("visit arraylit")
        if not self.arrflag:
            self.curr_arr = ast
            self.arrflag = True
        exprs = [self.visit(x, param) for x in ast.explist]
        #print(exprs)
        # get first element to typ of array
        first = exprs[0] if len(exprs) else None
        if not first: return AutoType()
        flag = False # co lenh xu ly int/float
        typlist = [first if type(first) is not ArrayType else first.typ]
        for i in range(1,len(exprs)):
            #typlist += [exprs[i] if type(exprs[i]) is not ArrayType else exprs[i].typ]
            if type(first) in [IntegerType, FloatType] and type(exprs[i]) in [IntegerType, FloatType]:
                typlist += [exprs[i]]
                continue
            if type(exprs[i]) is not type(first): raise IllegalArrayLiteral(self.curr_arr)
            if type(first) is ArrayType:
                # check dimen + typ of element
                if type(first.typ) in [IntegerType, FloatType] and type(exprs[i].typ) in [IntegerType, FloatType]:
                    typlist += [exprs[i].typ]
                if first.dimensions != exprs[i].dimensions: raise IllegalArrayLiteral(self.curr_arr)
                if type(first.typ) is not type(exprs[i].typ): raise IllegalArrayLiteral(self.curr_arr)
        
        for x in typlist:
            if type(x) is FloatType:
                flag = True
                break
        
        if type(first) is ArrayType:
            for x in typlist:
                if type(x) is FloatType:
                    flag = True
                    break
            #print(ArrayType([len(exprs)] + first.dimensions, first.typ if not flag else FloatType()))
            return ArrayType([len(exprs)] + first.dimensions, first.typ if not flag else FloatType())
        
        #print(ArrayType([len(exprs)], first if not flag else FloatType()))
        return ArrayType([len(exprs)], first if not flag else FloatType())
        
    
    def visitFuncCall(self, ast, param):
        #print("visit funcCall")
        func = None
        if ast.name =='super':
            func = Utils().lookup(self.curr_func.inherit, self.prototype, lambda x: x.name) 
        else:
            func = Utils().lookup(ast.name, param[-1], lambda x: x.name) 
            if not func: func = Utils().lookup(ast.name, self.prototype, lambda x: x.name) 
            
        #print(func.name)
        if not func: raise Undeclared(Function(), ast.name)
        if type(func.typ) is VoidType: raise TypeMismatchInExpression(ast)
        args = [self.visit(x, param) for x in ast.args]
        if(len(func.params) != len(args)): raise TypeMismatchInExpression(ast)
            # check type
        for i in range(len(args)):
            if type(func.params[i].typ) is AutoType:
                func.params[i].typ = args[i]
            if type(func.params[i].typ) is not type(args[i]): raise TypeMismatchInExpression(ast)
        return func.typ

    ##### Statements #####
    def visitAssignStmt(self, ast, param):
        #print('visit assignStmt')
        #print("current function:", self.curr_func.name)
        lhs = self.visit(ast.lhs, param)
        rhs = self.visit(ast.rhs, param)
        if type(lhs) is ArrayType and type(rhs) is ArrayType:
            if lhs.dimensions != rhs.dimensions:
                raise TypeMismatchInStatement(ast)
            if type(lhs.typ) is FloatType and type(rhs.typ) is IntegerType:
                self.arrflag = False
                self.curr_arr = None
                return lhs # tra ve type cua lhs  
                
            if type(lhs.typ) is not type(rhs.typ):
                raise TypeMismatchInExpression(ast)
        if type(lhs) is AutoType:
            if type(rhs) is AutoType: raise TypeMismatchInStatement(ast)
            lhs = InferType.infer(ast.lhs.name, rhs, param)
        if type(lhs) is VoidType:
            raise TypeMismatchInStatement(ast)
        if type(rhs) is AutoType:
            if type(ast.rhs) in [BinExpr, UnExpr]:
                self.typeinfer = lhs
                #print(self.typeinfer)
                #print(ast.rhs)
                # visit again bin to infer type operand
                rhs = self.visit(ast.rhs, param)
                if not type(rhs): raise TypeMismatchInStatement(ast)
                #print(rhs)
                self.typeinfer = None
            else:
                found = Utils().lookup(ast.rhs.name, self.prototype, lambda x: x.name)
                found.typ = lhs
                rhs = found.typ
            #print(found.typ)
        if type(lhs) is FloatType and type(rhs) is IntegerType: pass
            
        elif type(lhs) != type(rhs): raise TypeMismatchInStatement(ast)
        ##print(list(map(lambda x: (x.name, x.typ), param[1])))
        self.arrflag = False
        self.curr_arr = None
        return lhs # tra ve type cua lhs  
        
    def visitBlockStmt(self, ast, param):
        #print("visit blockstmt")
        # tao moi truong local cho new scope
        #local = [[]] + param
        ##print(list(map(lambda x: x.name, param[-1])))
        # check blockscope cua function => true: xu ly super, preventDefautl
        #print(param)
        func = None
        if param[1] != []:
            func = param[1][-1]
        #print(func.name, 'is function' if type(func) is FuncSymbol else 'is not function')
        #print(list(map(lambda x: x.name, param[0])))
        if type(func) is FuncSymbol and func.inherit != None:
            parent = Utils().lookup(func.inherit, list(filter(lambda x: type(x) is FuncSymbol, self.prototype)),lambda x: x.name)
            if parent is None: raise Undeclared(Function(), func.inherit)
            first = ast.body[0] if len(ast.body) != 0 else None # first stmt in body of function
            if not first or type(first) != CallStmt or first.name not in ['super', 'preventDefault']:
                # call super()
                if len(parent.params) != 0: raise InvalidStatementInFunction(func.name)
            
        for stmt in ast.body:
            #print(stmt)
            local = [[]] + param if  type(stmt) is BlockStmt else param
            self.visit(stmt, local)

    def visitIfStmt(self, ast, param):
        #print("visit ifstmt")
        # output cua expr cond must be boolean
        cond = self.visit(ast.cond, param)
        if type(cond) is not BooleanType: raise TypeMismatchInStatement(ast)
        # tao scope cho if stmt
        local = [[]] + param
        #print("true stmt")
        self.visit(ast.tstmt, local)
        self.returned = False
        if ast.fstmt:
            local[0] = []
            #print('false stmt')
            self.visit(ast.fstmt, local)
            self.returned = False
        
    def visitForStmt(self, ast, param):
        #print("visit for stmt")
        self.inloop += ['for']
        local = [[]] + param
        local[0] += [VarSymbol(ast.init.lhs.name,AutoType())]
        init = self.visit(ast.init, local)
        if type(init) is not IntegerType: raise TypeMismatchInStatement(ast)
        cond = self.visit(ast.cond, local)
        if type(cond) is not BooleanType: raise TypeMismatchInStatement(ast)
        updt = self.visit(ast.upd, local)
        if type(updt) is not IntegerType: raise TypeMismatchInStatement(ast)
        #print(list(map(lambda x: x.name, local[0])))
        self.visit(ast.stmt, local)
        self.returned = False
        self.inloop.pop(-1)
    def visitWhileStmt(self, ast, param): 
        #print("visit While stmt")
        self.inloop.append('while')
        if type(self.visit(ast.cond, param)) is not BooleanType: raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt, param)
        self.returned = False
        self.inloop.pop(-1)
    def visitDoWhileStmt(self, ast, param): 
        #print("visit do-while stmt")
        self.inloop.append("do-while")
        if type(self.visit(ast.cond, param)) is not BooleanType: raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt, param)
        self.returned = False
        self.inloop.pop(-1)
    def visitBreakStmt(self, ast, param):
        #print("break")
        if(self.inloop == []): raise MustInLoop(ast)
    def visitContinueStmt(self, ast, param):
        #print("continue")
        if(self.inloop == []): raise MustInLoop(ast)
    def visitReturnStmt(self, ast, param):
        #print("return stmt")
        if self.returned: return
        self.returned = True
        found = Utils().lookup(self.curr_func.name,self.prototype, lambda x: x.name)
        if not ast.expr:
            if type(self.curr_func.typ) is AutoType: found.typ = VoidType()
            elif type(self.curr_func.typ) is not VoidType: raise TypeMismatchInStatement(ast)
        else:
            infertyp = self.visit(ast.expr, param)
            if type(self.curr_func.typ) is AutoType:
                if type(infertyp) in [AutoType, VoidType]: raise TypeMismatchInStatement(ast)
                else: found.typ = infertyp        
            if type(self.curr_func.typ) is VoidType: raise TypeMismatchInStatement(ast)
            if type(self.curr_func.typ) is FloatType and type(infertyp) is IntegerType: infertyp = self.curr_func.typ
            if type(self.curr_func.typ) is not type(infertyp): raise TypeMismatchInStatement(ast)
        self.arrflag = False
        self.curr_arr = None
        
    def visitCallStmt(self, ast, param): 
        #print("visit callstmt")
        # check callfunc is declared
        # with super
        # get list pram of funccall, callstmt
        args = [self.visit(x, param) for x in ast.args]
        #print(args)
        if ast.name == 'super':
            parentF = Utils().lookup(self.curr_func.inherit, self.prototype, lambda x: x.name)
            if not parentF: raise TypeMismatchInStatement(ast)
            if len(args) < len(parentF.params): raise TypeMismatchInExpression(None)
            if len(args) > len(parentF.params): raise TypeMismatchInExpression(ast.args[len(parentF.params)])              
            for i in range(len(args)):
                if type(parentF.params[i].typ) is AutoType:
                    parentF.params[i].typ = args[i]
                if type(args[i]) is AutoType:
                    args[i] = parentF.params[i].typ
                #print(type(args[i]), '-', type(parentF.params[i].typ))
                if type(args[i]) is IntegerType and type(parentF.params[i].typ) is FloatType:
                    args[i] = parentF.params[i].typ
                if type(args[i]) != type(parentF.params[i].typ): raise TypeMismatchInExpression(ast.args[i])
            
        else:
            callfunc = Utils().lookup(ast.name, param[-1], lambda x: x.name)
            if callfunc is None:
                callfunc = Utils().lookup(ast.name, self.prototype, lambda x: x.name)
                if callfunc is None or type(callfunc) is not FuncSymbol: raise Undeclared(Function(), ast.name)
            else: 
                if type(callfunc) not in [FuncSymbol, GlobalFunc]: raise Undeclared(Function(), ast.name)
            
            
            #print(args)
            #print(callfunc.params)
            # check length cua 2 func
            if(len(callfunc.params) != len(args)): raise TypeMismatchInStatement(ast)
            # check type
            for i in range(len(args)):
                if type(callfunc.params[i].typ) is AutoType:
                    callfunc.params[i].typ = args[i]
                if type(args[i]) is AutoType:
                    args[i] = callfunc.params[i].typ
                if type(args[i]) is IntegerType and type(callfunc.params[i].typ) is FloatType:
                    args[i] = callfunc.params[i].typ
                if type(callfunc.params[i].typ) is not type(args[i]): raise TypeMismatchInStatement(ast)
            
    ##### Declared #####
    def visitVarDecl(self, ast, param):
        #print("visit Vardecl")
        if Utils().lookup(ast.name, param[0], lambda x: x.name) is not None:
            raise Redeclared(Variable(), ast.name) 
        self.curr_var = ast.name
        # full declared
        if ast.init is not None:
            rhstype = self.visit(ast.init, param) # lay type cua rhs
            #print(ast.typ)
            #print(rhstype)
            if type(ast.typ) is AutoType and type(rhstype) is AutoType: raise TypeMismatchInVarDecl(ast)
            # handle with auto type => infer type
            if type(rhstype) is ArrayType and type(ast.typ) is ArrayType:
                # check dimension
                if ast.typ.dimensions != rhstype.dimensions :
                    raise TypeMismatchInVarDecl(ast)
                if type(ast.typ.typ) is FloatType and type(rhstype.typ) is IntegerType:
                    param[0] += [VarSymbol(ast.name, ast.typ)]
                    self.arrflag = False
                    self.curr_arr = None
                    self.curr_var = None
                    return param
                if type(ast.typ.typ) is not type(rhstype.typ):
                    raise TypeMismatchInVarDecl(ast)
                
            if type(rhstype) in [BooleanType, IntegerType, FloatType, StringType, ArrayType]:
                if type(ast.typ) is AutoType or (type(ast.typ) == type(rhstype)) or type(ast.typ) is FloatType and type(rhstype) is IntegerType:
                    param[0] += [VarSymbol(ast.name, ast.typ if type(ast.typ) is not AutoType else rhstype)]
                    self.arrflag = False
                    self.curr_arr = None
                    self.curr_var = None
                    return param
                else: raise TypeMismatchInVarDecl(ast)
            elif type(ast.typ) in [BooleanType, IntegerType, FloatType, StringType, ArrayType] and type(rhstype) is AutoType:
                # tim kiem func symbol rhs trong symbol table
                #print(ast.init)
                if type(ast.init) not in [BinExpr, UnExpr]:
                    found = None
                    for syms in param:
                        found = Utils().lookup(ast.name, syms, lambda x: x.name)
                        if found: break
                    if not found: raise Undeclared(Function() if type(ast.init) is FuncCall else Identifier(), ast.name) 
                else:
                    self.typeinfer = ast.typ
                    #print(self.typeinfer)
                # visit again bin to infer type operand
                    tmp = self.visit(ast.init, param)
                    if not type(tmp): raise TypeMismatchInStatement(ast)
                    self.typeinfer = None
            else: raise TypeMismatchInVarDecl(ast)
        
        if ast.init is None:
            if type(ast.typ) is AutoType: raise Invalid(Variable(), ast.name)
            elif type(ast.typ) in [BooleanType, IntegerType, FloatType, StringType, ArrayType]:
                param[0] += [VarSymbol(ast.name, ast.typ)]
            else: raise TypeMismatchInVarDecl(ast)
        self.curr_var = None
        self.arrflag = False
        self.curr_arr = None
                
    def visitParamDecl(self, ast, param):
        paramSym = Utils().lookup(ast.name,param,lambda x: x.name)
        if paramSym != None: raise Redeclared(Parameter(), ast.name)
        param += [ParamSymbol(ast.name,ast.typ, ast.inherit, ast.out)]
        return param
    def visitFuncDecl(self, ast, param): 
        # check xem co redeclare
        # param[-1]: global scope
        funcsym = Utils().lookup(ast.name,param[-1], lambda x: x.name)
        if funcsym != None: raise Redeclared(Function(), ast.name)
        # get list param
        params = [] # luu parameter cua func con
        parentFunc = None
        if ast.inherit != None:
            # co ke thua => tim func cha
            ##print(list(map(lambda x: x.name,filter(lambda x: type(x) is FuncSymbol, self.prototype))))
            parentFunc = Utils().lookup(ast.inherit, list(filter(lambda x: type(x) is FuncSymbol, self.prototype)), lambda x: x.name)
            if parentFunc is None: raise Undeclared(Function(), ast.inherit)
            # tim thay ham cha trong global scope => get paramdecl has inherit keyword
            for x in parentFunc.params:
                if x.inherit: params += [x]
        
        idxInherit = len(params) # luu so luong param dc inherit tu ham cha
        for x in ast.params:
            if parentFunc:  
                if x.name in list(map(lambda x: x.name, parentFunc.params)): raise Invalid(Parameter(), x.name)
            params = self.visit(x, params)
        local_param = params[idxInherit:]
        #func = FuncSymbol(ast.name, local_param, ast.return_type, ast.inherit)
        func = Utils().lookup(ast.name, self.prototype, lambda x: x.name)
        param[-1] += [func]
        # get all param cua func cha dua vao local
        local = [params] + param # scope cua ham
        # vieng tham body
        self.curr_func = func
        self.visit(ast.body, local)
        self.curr_func = None
        self.returned = False

    ##### Program #####
    def visitProgram(self, ast, param):
        # first get prototype 
        self.prototype = GetPrototype(self.ast).visit(self.ast, param)
        #print(list(map(lambda x: x.name if type(x) is VarSymbol or type(x) is GlobalFunc else f'func {x.typ} {x.name}({list(map(lambda y: (y.name, y.typ), x.params))})', self.prototype)))
        for decl in ast.decls:
            self.visit(decl,self.env)
        
        #print(list(map(lambda x: x.name if type(x) is VarSymbol or type(x) is GlobalFunc else f'func {x.typ} {x.name}({list(map(lambda y: (y.name, y.typ), x.params))})', self.env[0])))
        ismain = False
        #print(list(map(lambda x: x.name, param[0])))
        for func in self.env[0]:
            if type(func) is FuncSymbol and func.name == 'main' and type(func.typ) is VoidType and func.params == []:
                ismain = True
                break
        
        if not ismain: raise NoEntryPoint() 