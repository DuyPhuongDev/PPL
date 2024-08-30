from functools import reduce

from Frame import Frame
from Emitter import *
from abc import ABC
from Visitor import *
from AST import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None, parent=None):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.parent = parent

    def __str__(self):
        return "Symbol(" + self.name + "," + str(self.mtype) + ")"

class SubBody():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value


class CName(Val):
    def __init__(self, value):
        self.value = value

class ClassType(Type):
    def __init__(self, classname) -> None:
        self.classname = classname
    def __str__(self):
        return "ClassType"
    def accept(self, v, param):
        return v.visitClassType(self, param)
        
class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [[Symbol("readInteger", MType(list(), IntegerType()), CName(self.libName)),
                Symbol("printInteger", MType([IntegerType()], VoidType()), CName(self.libName)),
                Symbol("readFloat", MType([], FloatType()), CName(self.libName)),
                Symbol("writeFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("readBoolean", MType([], BooleanType()), CName(self.libName)),
                Symbol("printBoolean", MType([BooleanType()], VoidType()), CName(self.libName)),
                Symbol("readString", MType([], StringType()), CName(self.libName)),
                Symbol("printString", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("preventDefault", MType([], VoidType()), CName(self.libName))]
                #Symbol("super", MType([], FloatType()), CName(self.libName)),
                
                ]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, None)
 
class CodeGenVisitor(Visitor, Utils):
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.path = path
        self.className = "MT22Class"
        self.emit = Emitter(path + "/" + self.className +".j")
        self.hasStaticfield = False
        self.glcode = ""
        self.glframe = Frame("global", VoidType())
        self.hasReturn = False
        self.parfunc = None
        self.prototype = []
        self.typArr = None
        self.conflag = None
        self.isFor = False
        self.returned = False
        
    def genMETHOD(self, consdecl: FuncDecl, o: List[Symbol], frame: Frame):
        # contsdecl: FuncDecl
        # o: list[Symbol]
        # frame: Frame
        #print("gen method: " + consdecl.name)
        
        isInit = consdecl.name == "<init>" and len(consdecl.params) == 0 and type(consdecl.return_type) is VoidType and consdecl.inherit is None  # constructor
        isMain = consdecl.name == "main" and len(consdecl.params) == 0 and type(consdecl.return_type) is VoidType and consdecl.inherit is None
        return_type = VoidType() if isInit else consdecl.return_type
        methodName = "<init>" if isInit else consdecl.name
        
        # param: if main => (String[] args) else ()
        
        #intype = [ArrayType([], StringType())] if isMain else []
        if isMain:
            intype = [ArrayType([], StringType())]
        elif isInit:
            intype = []
        else:
             intype = [x.typ for x in consdecl.params]   
        mtype = MType(intype, return_type)
        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        #glenv = o
        local = SubBody(frame, [[]]+o if o != None else [[]]) 
        #if not isInit: print(list(map(lambda x: x.name, local.sym[1])))
        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([1],StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            for x in consdecl.params:
                local = self.visit(x, local)
        
        #if not isInit: print(list(map(lambda x: x.name, local.sym[0])))        
        body = consdecl.body
        # for stmt in body.body:
        #     print(stmt)
            
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        else:
        #list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.body))
            for stmt in body.body:
                if type(stmt) is ReturnStmt: self.returned = True
                self.visit(stmt, local)

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(return_type) is VoidType and self.hasReturn == False:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        elif not self.returned: self.emit.printout(self.emit.emitRETURN(return_type, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        self.hasReturn = False
        self.returned = False
        frame.exitScope()


    def visitBinExpr(self, ast: BinExpr, param: Access):
        e1c, e1t = self.visit(ast.left, param)
        e2c, e2t = self.visit(ast.right, param)
        if type(e1t) is type(e2t):
            rt = e1t
        else:
            if type(e1t) is FloatType and type(e2t) is IntegerType:
                e2c = e2c + self.emit.emitI2F(param.frame)
                rt = e1t
            elif type(e1t) is IntegerType and type(e2t) is FloatType:
                e1c = e1c + self.emit.emitI2F(param.frame)
                rt = e2t
        
        if ast.op in ['+', '-']:
            code = self.emit.emitADDOP(ast.op, rt, param.frame)
        elif ast.op in ['*']:
            code = self.emit.emitMULOP(ast.op, rt, param.frame)
        elif ast.op in ['/']:
            if type(e1t) is IntegerType and type(e2t) is IntegerType:
                e1c = e1c + self.emit.emitI2F(param.frame)
                e2c = e2c + self.emit.emitI2F(param.frame)
                rt = FloatType()
            code = self.emit.emitMULOP(ast.op, rt, param.frame)
        elif ast.op in ['%']:
            code = self.emit.emitMOD(param.frame)
        elif ast.op == '&&':
            code = self.emit.emitANDOP(param.frame)
        elif ast.op == '||':
            code = self.emit.emitOROP(param.frame)
        elif ast.op == '::':
            code = self.emit.emitINVOKEVIRTUAL('java/lang/String/concat', MType([StringType()], StringType()), param.frame)
        elif ast.op in ['==', '!=', '<', '>', '<=', '>=']:
            rt = BooleanType()
            code = self.emit.emitREOP(ast.op, rt, param.frame)
        return e1c + e2c + code, rt
            

    def visitUnExpr(self, ast: UnExpr, param: Access):
        ec ,et = self.visit(ast.val, param)
        if ast.op == '-':
            code = self.emit.emitNEGOP(et, param.frame)
        elif ast.op == '!':
            code = self.emit.emitNOT(et, param.frame)
        return ec + code, et

    def visitId(self, ast: Id, param: Access): 
        #print("visit id: " + ast.name)
        found = None
        for env in param.sym:
            found = Utils().lookup(ast.name, env,lambda x: x.name)
            if found: break
            
        if param.isLeft: # store
            if type(found.value) is Index:
                code = self.emit.emitWRITEVAR(found.name, found.mtype, found.value.value, param.frame)
            else:
                code = self.emit.emitPUTSTATIC(found.value.value + "." + found.name, found.mtype,param.frame)
        else:
            if type(found.value) is Index:
                code = self.emit.emitREADVAR(found.name, found.mtype, found.value.value, param.frame)
            else:
                code = self.emit.emitGETSTATIC(found.value.value + "." + found.name, found.mtype, param.frame)
        return code, found.mtype
            

    def visitArrayCell(self, ast: ArrayCell, param: Access):
        found: Symbol = list(filter(lambda x: x.name == ast.name, [sym for env in param.sym for sym in env]))[0]
        buff = list()
        buff.append(self.emit.emitREADVAR(ast.name, found.mtype, found.value.value, param.frame))
        for i in range(len(ast.cell)-1):
            ec, et = self.visit(ast.cell[i], Access(param.frame, param.sym, False))
            buff.append(ec)
            buff.append(self.emit.emitALOAD(found.mtype,param.frame))
        
        ec, et = self.visit(ast.cell[-1], Access(param.frame, param.sym, False))
        buff.append(ec)
        if not param.isLeft:
            #print(found.mtype)
            buff.append(self.emit.emitALOAD(found.mtype.typ if type(found.mtype) is ArrayType else found.mtype, param.frame))
        res = ''.join(buff)
        return res, found.mtype.typ if type(found.mtype) is ArrayType else found.mtype

    def visitIntegerLit(self, ast: IntegerLit, param: Access): 
        if param.isFirst:
            return IntegerType()
        code = self.emit.emitPUSHICONST(ast.val,param.frame)
        return code, IntegerType()
    
    def visitFloatLit(self, ast: FloatLit, param: Access): 
        if param.isFirst: return FloatType()
        code = self.emit.emitPUSHFCONST(str(ast.val),param.frame)
        return code, FloatType()
        
    def visitStringLit(self, ast: StringLit, param: Access):
        if param.isFirst: return StringType()
        code = self.emit.emitPUSHCONST('"' + ast.val + '"', StringType(), param.frame)
        return code, StringType()

    def visitBooleanLit(self, ast: BooleanLit, param):
        if param.isFirst: return BooleanType()
        code = self.emit.emitPUSHICONST('true' if ast.val else 'false', param.frame)
        return code, BooleanType()

    def visitArrayLit(self, ast: ArrayLit, param: Access):
        if param.isFirst:
            for exp in ast.explist:
                typ = self.visit(exp, Access(param.frame, param.sym, False, True))
            dimen = [len(ast.explist)]
            dimen += typ.dimensions if type(typ) is ArrayType else []
            return ArrayType(dimen, typ.typ if type(typ) is ArrayType else typ)
        else:
            buff = list() 
            exprs = [self.visit(x, Access(param.frame, param.sym, False, True)) for x in ast.explist]
            first = exprs[0] if len(exprs) else self.typArr
            buff.append(self.emit.emitNEWARRAY(first, len(ast.explist), param.frame))
            # self.typArr = ArrayType(self.typArr.dimensions[1:], self.typArr.typ) if ast.explist and type(ast.explist[0]) is ArrayLit else self.typArr
            for i in range(len(ast.explist)):
                buff.append(self.emit.emitDUP(param.frame))
                buff.append(self.emit.emitPUSHICONST(i, param.frame))
                ec, et = self.visit(ast.explist[i], Access(param.frame, param.sym, False))
                buff.append(ec)
                buff.append(self.emit.emitAASTORE(et,param.frame))
            res = ''.join(buff)
            #print(res)
            dimen = [len(ast.explist)]
            dimen += et.dimensions if type(et) is ArrayType else []
            return res, ArrayType(dimen, et.typ if type(et) is ArrayType else et)

    def visitFuncCall(self, ast: FuncCall, param: Access):
        funcName = self.parfunc if ast.name == 'super' else ast.name
        specFunc = ['readInteger', 'printInteger', 'readFloat', 'writeFloat', 'readBoolean', 'printBoolean', 'readString', 'printString']
        args = ast.args
        found = None
        for env in param.sym:
            found = Utils().lookup(funcName, env, lambda x: x.name)
            if found: break
        if not found: found = Utils().lookup(funcName, self.prototype, lambda x: x.name)
        buff = []
        for arg in args:
            ac, at = self.visit(arg, Access(param.frame, param.sym, False))
            buff.append(ac)
        clname = self.className if funcName not in specFunc else 'io'
        buff.append(self.emit.emitINVOKESTATIC(clname +'/'+funcName, found.mtype, param.frame))
        #buff.append(self.emit.emitINVOKESTATIC(self.className+'/'+funcName, found.mtype, param.frame))
        res = "".join(buff)
        return res, found.mtype.rettype

    def visitAssignStmt(self, ast: AssignStmt, param: SubBody):
        # load rhs
        rc, rt = self.visit(ast.rhs, Access(param.frame, param.sym, False))
        lc, lt = self.visit(ast.lhs, Access(param.frame, param.sym, True))
        if type(ast.lhs) is ArrayCell:
            self.emit.printout(lc+rc+ self.emit.emitASTORE(lt, param.frame))
        else: self.emit.printout(rc+lc)

    def visitBlockStmt(self, ast: BlockStmt, param: SubBody):
        # create new scope
        param.frame.enterScope(False)
        # tao moi truong local cho scope
        local = SubBody(param.frame, [[]] + param.sym)
        self.emit.printout(self.emit.emitLABEL(param.frame.getStartLabel(), param.frame))
        for stmt in ast.body:
            self.visit(stmt, local)
        self.emit.printout(self.emit.emitLABEL(param.frame.getEndLabel(), param))
        param.frame.exitScope()
        # for env in local.sym:
        #     print(list(map(lambda x: (x.name, x.mtype), env)))

    def visitIfStmt(self, ast: IfStmt, param: SubBody):
        # gen code for cond expr
        ec, et = self.visit(ast.cond, Access(param.frame, param.sym, False))
        self.emit.printout(ec)
        # xin tu frame Flabel
        flabel = param.frame.getNewLabel()
        # if false => jump to Flabel
        self.emit.printout(self.emit.emitIFFALSE(flabel, param.frame))
        # gen code tstmt
        self.visit(ast.tstmt, param)
        if ast.fstmt is None:
            # dat flabel here
            self.emit.printout(self.emit.emitLABEL(flabel, param.frame))
        else:
            # xin tu frame elabel
            elabel = param.frame.getNewLabel()
            # nhay toi elabel
            self.emit.printout(self.emit.emitGOTO(elabel, param.frame))
            # dat flabel o day
            self.emit.printout(self.emit.emitLABEL(flabel, param.frame))
            # gen code fstmt
            self.visit(ast.fstmt, param)
            # dat elabel o day
            self.emit.printout(self.emit.emitLABEL(elabel, param.frame))

    def visitForStmt(self, ast: ForStmt, param: SubBody): 
        self.isFor = True
        # sinh ma init expr
        found = None
        for env in param.sym:
            found = Utils().lookup(ast.init.lhs.name, env, lambda x: x.name)
            if found: break
        # khai bao bien i
        local = [[]] + param.sym
        param.frame.enterLoop()
        condLabel = param.frame.getContinueLabel()
        brkLabel = param.frame.getBreakLabel()
        if not found:
            idx = param.frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx,ast.init.lhs.name,IntegerType(),condLabel, brkLabel, param.frame))
            found = Symbol(ast.init.lhs.name, IntegerType(),Index(idx))
            local[0] += [found]
        self.visit(ast.init, SubBody(param.frame, local))
        
        
        # dat label continue
        self.emit.printout(self.emit.emitLABEL(condLabel, param.frame))

        # gencode cho cond expr
        ec, et = self.visit(ast.cond, Access(param.frame, local, False))
        self.emit.printout(ec)
        self.emit.printout(self.emit.emitIFFALSE(brkLabel, param.frame))
        self.conflag = param.frame.getNewLabel()
        self.visit(ast.stmt, SubBody(param.frame, local))
       
        self.emit.printout(self.emit.emitLABEL(self.conflag, param.frame))
        # gen code update expr
        uc, ut = self.visit(ast.upd, Access(param.frame, local, False))
        self.emit.printout(uc)
        # update var i
        self.emit.printout(self.emit.emitWRITEVAR(ast.init.lhs.name, IntegerType(), found.value.value ,param.frame))
        # nhay den continue label
        self.emit.printout(self.emit.emitGOTO(condLabel, param.frame))
        # dat brklabel
        self.emit.printout(self.emit.emitLABEL(brkLabel,param.frame))
        param.frame.exitLoop()
        self.isFor = False

    def visitWhileStmt(self, ast: WhileStmt, param: SubBody): 
        param.frame.enterLoop()
        conLabel = param.frame.getContinueLabel()
        brkLabel = param.frame.getBreakLabel()
        # dat continue label 
        self.emit.printout(self.emit.emitLABEL(conLabel, param.frame))
        # sinh ma cho cond expr
        ec, et = self.visit(ast.cond, Access(param.frame, param.sym, False))
        self.emit.printout(ec)
        self.emit.printout(self.emit.emitIFFALSE(brkLabel, param.frame))
        self.visit(ast.stmt, param)
        self.emit.printout(self.emit.emitGOTO(conLabel, param.frame))
        # dat brk label
        self.emit.printout(self.emit.emitLABEL(brkLabel, param.frame))
        param.frame.exitLoop()

    def visitDoWhileStmt(self, ast: DoWhileStmt, param: SubBody):
        param.frame.enterLoop()
        conLabel = param.frame.getContinueLabel()
        brkLabel = param.frame.getBreakLabel()
        tmpLabel = param.frame.getNewLabel()
        self.emit.printout(self.emit.emitLABEL(tmpLabel, param.frame))
        self.visit(ast.stmt, param)
        # dat continue label 
        self.emit.printout(self.emit.emitLABEL(conLabel, param.frame))
        # sinh ma cho cond expr
        ec, et = self.visit(ast.cond, Access(param.frame, param.sym, False))
        self.emit.printout(ec)
        self.emit.printout(self.emit.emitIFFALSE(brkLabel, param.frame))
        self.emit.printout(self.emit.emitGOTO(tmpLabel, param.frame))
        # dat brk label
        self.emit.printout(self.emit.emitLABEL(brkLabel, param.frame))
        param.frame.exitLoop()

    def visitBreakStmt(self, ast: BreakStmt, param: SubBody):
        brkLabel = param.frame.getBreakLabel()
        self.emit.printout(self.emit.emitGOTO(brkLabel, param.frame))

    def visitContinueStmt(self, ast: ContinueStmt, param: SubBody):
        if self.isFor:

            self.emit.printout(self.emit.emitGOTO(self.conflag, param.frame))
        else:
            conLabel = param.frame.getContinueLabel()
            self.emit.printout(self.emit.emitGOTO(conLabel, param.frame))

    def visitReturnStmt(self, ast: ReturnStmt, param: SubBody):
        self.hasReturn = True
        if ast.expr:
            rc, rt = self.visit(ast.expr, Access(param.frame, param.sym, False))
            self.emit.printout(rc)
            self.emit.printout(self.emit.emitRETURN(rt, param.frame))
        else: self.emit.printout(self.emit.emitRETURN(VoidType(), param.frame))

    def visitCallStmt(self, ast: CallStmt, param: SubBody):
        funcName =  self.parfunc if ast.name == 'super' else ast.name
        
        specFunc = ['readInteger', 'printInteger', 'readFloat', 'writeFloat', 'readBoolean', 'printBoolean', 'readString', 'printString', 'preventDefault']

        args = ast.args
        found = None
        for env in param.sym:
            found = Utils().lookup(funcName, env, lambda x: x.name)
            if found: break
        if not found: found = Utils().lookup(funcName, self.prototype, lambda x: x.name)
        #print(found)
        for arg in args:
            ac, at = self.visit(arg, Access(param.frame, param.sym, False))
            self.emit.printout(ac)
        clname = self.className if funcName not in specFunc else 'io'

        self.emit.printout(self.emit.emitINVOKESTATIC(clname +'/'+funcName, found.mtype, param.frame))
        if type(found.mtype.rettype) != VoidType:
            self.emit.printout(self.emit.emitPOP(param.frame))

    def visitVarDecl(self, ast: VarDecl, param: SubBody): 
        #local var
        if param.frame is None:
            self.emit.printout(self.emit.emitATTRIBUTE(ast.name, ast.typ, False, None))
            if ast.init is not None: # khai bao co khoi tao gia tri
                # visit rhs cua vardecl
                if type(ast.typ) is ArrayType: self.typArr = ast.typ
                initCode, initType = self.visit(ast.init, Access(self.glframe, param.sym, False))
                i2f = self.emit.emitI2F(param.frame) if type(initType) is IntegerType and type(ast.typ) is FloatType else ''
                self.glcode = self.glcode + initCode + self.emit.emitPUTSTATIC(self.className + "." + ast.name,ast.typ, self.glframe)
            param.sym[0] += [Symbol(ast.name, ast.typ, CName(self.className))]
            return param
        else:
            # xin index moi tu frame
            newidx = param.frame.getNewIndex() 
            self.emit.printout(self.emit.emitVAR(newidx, ast.name, ast.typ, param.frame.getStartLabel(), param.frame.getEndLabel(), param.frame))
            if ast.init is not None:
                if type(ast.typ) is ArrayType: self.typArr = ast.typ
                initCode, initType = self.visit(ast.init, Access(param.frame, param.sym, False))
                i2f = self.emit.emitI2F(param.frame) if type(initType) is IntegerType and type(ast.typ) is FloatType else ''
                self.emit.printout(initCode + i2f + self.emit.emitWRITEVAR(ast.name, ast.typ,newidx,param.frame))
            param.sym[0] += [Symbol(ast.name, ast.typ, Index(newidx))]
            return param
    def visitParamDecl(self, ast: ParamDecl, param: SubBody): 
        # xin index moi
        newidx = param.frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(newidx,  ast.name, ast.typ, param.frame.getStartLabel(), param.frame.getEndLabel(), param.frame))
        param.sym[0] += [Symbol(ast.name, ast.typ, Index(newidx))]
        return param

    def visitFuncDecl(self, ast: FuncDecl, param: SubBody):
        self.parfunc = ast.inherit
        frame = Frame(ast.name, ast.return_type)
        patype = [x.typ for x in ast.params]
        param.sym[-1] += [Symbol(ast.name, MType(patype,ast.return_type),CName(self.className), ast.inherit)]
        self.genMETHOD(ast, param.sym, frame)
        self.parfunc = None
        return param

    def visitProgram(self, ast, param):
        self.emit.printout(self.emit.emitPROLOG(self.className, "java/lang/Object"))
        env = SubBody(None, self.env)
        for decl in ast.decls:
            if type(decl) is VarDecl and decl.init:
                self.hasStaticfield = True
                env = self.visit(decl, env)
            elif type(decl) is FuncDecl:
                self.prototype.append(Symbol(decl.name, MType([x.typ for x in decl.params], decl.return_type),CName(self.className), decl.inherit))
        # generate default constructor
        self.genMETHOD(FuncDecl("<init>", VoidType(), [], None,BlockStmt([])), param, Frame("<init>", VoidType()))
        #print(list(map(lambda x: x.name, self.prototype)))
        for decl in ast.decls:
            if type(decl) is FuncDecl:
                env = self.visit(decl, env)
                
        if self.hasStaticfield: self.genClinit(self.glcode, self.glframe)
        #print(list(map(lambda x: x.name, env.sym[-1])))
        self.emit.emitEPILOG()
        return param
    
    def genClinit(self, code , frame):
        self.emit.printout(self.emit.emitMETHOD("<clinit>",MType([], VoidType()), True, frame))
        self.emit.printout(code)
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))