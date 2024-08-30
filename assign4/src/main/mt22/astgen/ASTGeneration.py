from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    # program: decllist EOF ;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decllist()))
    
    # decllist: decl decllist | decl;
    def visitDecllist(self, ctx: MT22Parser.DecllistContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.decl())
        return self.visit(ctx.decl()) + self.visit(ctx.decllist())
    
    # decl: vardecl | funcdecl;
    def visitDecl(self, ctx: MT22Parser.DeclContext):
        if ctx.vardecl():
            res = self.visit(ctx.vardecl())
            return res
        return [self.visit(ctx.funcdecl())]
    
    # vardecl: idlist COLON typ SEMI_COLON | IDENTIFIERS listvar expr SEMI_COLON;
    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        if ctx.idlist():
            names = self.visit(ctx.idlist())
            typ = self.visit(ctx.typ())
            return [VarDecl(name, typ) for name in names]
        
        names , exprs, typ = self.visit(ctx.listvar())
        names = [ctx.IDENTIFIERS().getText()] + names
        exprs = exprs + [self.visit(ctx.expr())]
        return list(map(lambda name, expr: VarDecl(name, typ, expr), names, exprs))
    
    # listvar: COMMA IDENTIFIERS listvar expr COMMA | COLON typ ASSIGN;
    def visitListvar(self, ctx: MT22Parser.ListvarContext):
        if(ctx.typ()):
            return [], [], self.visit(ctx.typ())
        else:
            ids, exprs, typ = self.visit(ctx.listvar())
            return [ctx.IDENTIFIERS().getText()] + ids, exprs + [self.visit(ctx.expr())], typ
            
    # funcdecl: IDENTIFIERS COLON FUNCTION returntype paradecl (INHERIT IDENTIFIERS)? blockstmt;
    def visitFuncdecl(self, ctx: MT22Parser.FuncdeclContext):
        name = ctx.IDENTIFIERS(0).getText()
        return_type = self.visit(ctx.returntype())
        params = self.visit(ctx.paradecl())
        body = self.visit(ctx.blockstmt())
        inherit = ctx.IDENTIFIERS(1).getText() if ctx.INHERIT() else None
        return FuncDecl(name, return_type, params, inherit, body)
    
    # paradecl: LROUNDBR paramlist RROUNDBR;
    def visitParadecl(self, ctx: MT22Parser.ParadeclContext):
        return self.visit(ctx.paramlist())
    # paramlist: paramprime | ;
    def visitParamlist(self, ctx: MT22Parser.ParamlistContext):
        if ctx.paramprime():
            return self.visit(ctx.paramprime())
        return []
    # paramprime: param COMMA paramprime | param;
    def visitParamprime(self, ctx: MT22Parser.ParamprimeContext):
        if ctx.getChildCount() == 1: 
            return [self.visit(ctx.param())]
        return [self.visit(ctx.param())] + self.visit(ctx.paramprime())
    # param: INHERIT? OUT? IDENTIFIERS COLON typ;
    def visitParam(self, ctx: MT22Parser.ParamContext):
        inherit = True if ctx.INHERIT() else False
        out = True if ctx.OUT() else False
        name = ctx.IDENTIFIERS().getText()
        typ = self.visit(ctx.typ())
        return ParamDecl(name, typ, out, inherit)
    
    # typ: atomtype | arraytype | AUTO;
    def visitTyp(self, ctx: MT22Parser.TypContext):
        if ctx.atomtype(): return self.visit(ctx.atomtype())
        elif ctx.arraytype(): return self.visit(ctx.arraytype())
        return AutoType()
    # atomtype: BOOLEAN | INTEGER | FLOAT | STRING;
    def visitAtomtype(self, ctx: MT22Parser.AtomtypeContext):
        if ctx.BOOLEAN(): 
            return BooleanType()
        elif ctx.INTEGER(): return IntegerType()
        elif ctx.FLOAT(): return FloatType()
        elif ctx.STRING(): return StringType()
    # arraytype: ARRAY LSQUAREBR dimensions RSQUAREBR OF atomtype;
    def visitArraytype(self, ctx: MT22Parser.ArraytypeContext):
        dimensions = self.visit(ctx.dimensions())
        typ = self.visit(ctx.atomtype())
        return ArrayType(dimensions, typ)
    # dimensions: INTLIT COMMA dimensions | INTLIT;
    def visitDimensions(self, ctx: MT22Parser.DimensionsContext):
        if ctx.getChildCount() == 1: 
            return [int(ctx.INTLIT().getText())]
        return [int(ctx.INTLIT().getText())] + self.visit(ctx.dimensions())
    # returntype: VOID | atomtype | arraytype | AUTO;
    def visitReturntype(self, ctx: MT22Parser.ReturntypeContext):
        if ctx.VOID(): return VoidType()
        elif ctx.atomtype(): 
            return self.visit(ctx.atomtype())
        elif ctx.arraytype(): return self.visit(ctx.arraytype())
        elif ctx.AUTO(): return AutoType()
    
    # arraylit: LBRACES exprlist RBRACES;
    def visitArraylit(self, ctx: MT22Parser.ArraylitContext):
        exprs = self.visit(ctx.exprlist())
        return ArrayLit(exprs)
    
    # idlist: IDENTIFIERS COMMA idlist | IDENTIFIERS;
    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        if ctx.getChildCount() == 1:
            return [ctx.IDENTIFIERS().getText()]
        return [ctx.IDENTIFIERS().getText()] + self.visit(ctx.idlist())
    
    # # blockstmt: LBRACES stmtlist RBRACES;
    # def visitBlockstmt(self, ctx: MT22Parser.BlockstmtContext):
    #     body = self.visit(ctx.stmtlist())
    #     return BlockStmt(body)
    # # stmtlist: stmt stmtlist| ;
    # def visitStmtlist(self, ctx: MT22Parser.StmtlistContext):
    #     return [self.visit(ctx.stmt())] + self.visit(ctx.stmtlist()) if ctx.stmt() else []
    # # stmt: matchstmt | unmatchstmt | vardecl;
    # def visitStmt(self, ctx: MT22Parser.StmtContext):
    #     if ctx.matchstmt():
    #         return self.visit(ctx.matchstmt())
    #     elif ctx.unmatchstmt():
    #         return self.visit(ctx.unmatchstmt())
    #     return self.visit(ctx.vardecl())
    
    
    #blockstmt: LBRACES (body | ) RBRACES;
    #body: bodyprime body | bodyprime;
    #bodyprime: stmt | vardecl;
    #stmt: matchstmt | unmatchstmt;
    def visitBlockstmt(self, ctx: MT22Parser.BlockstmtContext):
        if ctx.body():
            body = self.visit(ctx.body())
            return BlockStmt(body)
        return BlockStmt([])
    
    def visitBody(self, ctx: MT22Parser.BodyContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.bodyprime())
        return self.visit(ctx.bodyprime()) + self.visit(ctx.body())
    
    def visitBodyprime(self, ctx: MT22Parser.BodyprimeContext):
        return [self.visit(ctx.stmt())] if ctx.stmt() else self.visit(ctx.vardecl())
    
    def visitStmt(self, ctx: MT22Parser.StmtContext):
        return self.visit(ctx.matchstmt()) if ctx.matchstmt() else self.visit(ctx.unmatchstmt())
    
    # matchstmt: matchifstmt | assignstmt | forstmt | whilestmt | 
    # dowhilestmt | breakstmt | contstmt | returnstmt | callstmt | blockstmt;
    def  visitMatchstmt(self, ctx: MT22Parser.MatchstmtContext):
        if ctx.matchifstmt(): return self.visit(ctx.matchifstmt())
        elif ctx.assignstmt(): return self.visit(ctx.assignstmt())
        elif ctx.forstmt(): return self.visit(ctx.forstmt())
        elif ctx.whilestmt(): return self.visit(ctx.whilestmt())
        elif ctx.dowhilestmt(): return self.visit(ctx.dowhilestmt())
        elif ctx.breakstmt(): return self.visit(ctx.breakstmt())
        elif ctx.contstmt(): return self.visit(ctx.contstmt())
        elif ctx.returnstmt(): return self.visit(ctx.returnstmt())
        elif ctx.callstmt(): return self.visit(ctx.callstmt())
        elif ctx.blockstmt(): return self.visit(ctx.blockstmt())
    
    # unmatchstmt: IF LROUNDBR expr RROUNDBR stmt 
    #            | IF LROUNDBR expr RROUNDBR matchstmt ELSE unmatchstmt;
    def visitUnmatchstmt(self,  ctx: MT22Parser.UnmatchstmtContext):
        cond = self.visit(ctx.expr())
        if ctx.ELSE():
            matchstmt = self.visit(ctx.matchstmt())
            unmatchstmt = self.visit(ctx.unmatchstmt())
            return IfStmt(cond, matchstmt, unmatchstmt)
        return IfStmt(cond, self.visit(ctx.stmt()))
    #matchifstmt: IF LROUNDBR expr RROUNDBR matchstmt ELSE matchstmt;
    def visitMatchifstmt(self, ctx: MT22Parser.MatchifstmtContext):
        expr = self.visit(ctx.expr())
        return IfStmt(expr, self.visit(ctx.matchstmt(0)), self.visit(ctx.matchstmt(1)))
    # assignstmt: scalavar ASSIGN expr SEMI_COLON;
    def visitAssignstmt(self, ctx: MT22Parser.AssignstmtContext):
        lhs = self.visit(ctx.scalavar())
        rhs = self.visit(ctx.expr())
        # print(rhs)
        return AssignStmt(lhs, rhs)
            
    # forstmt: FOR LROUNDBR scaladecl COMMA conditionexpr COMMA updateExpr RROUNDBR stmt;
    def visitForstmt(self, ctx: MT22Parser.ForstmtContext):
        init = self.visit(ctx.scaladecl())
        cond = self.visit(ctx.conditionexpr())
        upd = self.visit(ctx.updateExpr())
        stmt = self.visit(ctx.stmt())
        return ForStmt(init, cond, upd, stmt)
    # scaladecl: scalavar ASSIGN expr;
    def visitScaladecl(self, ctx: MT22Parser.ScaladeclContext):
        name = self.visit(ctx.scalavar())
        expr = self.visit(ctx.expr())
        return AssignStmt(name, expr)
    # conditionexpr: expr;
    def visitConditionexpr(self, ctx: MT22Parser.ConditionexprContext):
        return self.visit(ctx.expr())
    # updateExpr: expr;
    def visitUpdateExpr(self, ctx: MT22Parser.UpdateExprContext):
        return self.visit(ctx.expr())
    # whilestmt: WHILE LROUNDBR expr RROUNDBR stmt;
    def visitWhilestmt(self, ctx: MT22Parser.WhilestmtContext):
        return WhileStmt(self.visit(ctx.expr()), self.visit(ctx.stmt()))
    # dowhilestmt: DO blockstmt WHILE LROUNDBR expr RROUNDBR SEMI_COLON;
    def visitDowhilestmt(self, ctx:MT22Parser.DowhilestmtContext):
        cond = self.visit(ctx.expr())
        stmt = self.visit(ctx.blockstmt())
        return DoWhileStmt(cond, stmt)
    # breakstmt: BREAK SEMI_COLON;
    def visitBreakstmt(self, ctx: MT22Parser.BreakstmtContext):
        return BreakStmt()
    # contstmt: CONTINUE SEMI_COLON;
    def visitContstmt(self, ctx: MT22Parser.ContstmtContext):
        return ContinueStmt()
    # returnstmt: RETURN (expr | ) SEMI_COLON;
    def visitReturnstmt(self, ctx: MT22Parser.ReturnstmtContext):
        if ctx.expr():
            expr = self.visit(ctx.expr())
            return ReturnStmt(expr)
        return ReturnStmt(None)
    # callstmt: IDENTIFIERS LROUNDBR exprlist RROUNDBR SEMI_COLON; // use in statements
    def visitCallstmt(self, ctx: MT22Parser.CallstmtContext):
        name = ctx.IDENTIFIERS().getText()
        exprs = self.visit(ctx.exprlist())
        return CallStmt(name, exprs)
    
    # idxop: IDENTIFIERS LSQUAREBR exprprime RSQUAREBR;
    def visitIdxop(self, ctx: MT22Parser.IdxopContext):
        name = ctx.IDENTIFIERS().getText()
        cell = self.visit(ctx.exprprime())
        return ArrayCell(name, cell)
    # exprlist: exprprime | ;
    def visitExprlist(self, ctx: MT22Parser.ExprlistContext):
        if ctx.exprprime():
            return self.visit(ctx.exprprime())
        return []
    # exprprime: expr COMMA exprprime | expr;
    def visitExprprime(self, ctx: MT22Parser.ExprprimeContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.expr())] + self.visit(ctx.exprprime())
        return [self.visit(ctx.expr())]
    # expr: expr1 DBCOLON expr1 | expr1;
    def visitExpr(self, ctx: MT22Parser.ExprContext):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.expr1(0))
            right = self.visit(ctx.expr1(1))
            return BinExpr(ctx.DBCOLON().getText(),left, right)
        return self.visit(ctx.expr1(0))
    # expr1: expr2 (EQUAL | NOTEQUAL | LESSEQUAL | LESS | GREATER | GREATEREQUAL) expr2 | expr2;
    def visitExpr1(self, ctx: MT22Parser.Expr1Context):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.expr2(0))
            right = self.visit(ctx.expr2(1))
            if ctx.EQUAL(): return BinExpr(ctx.EQUAL().getText(),left, right)
            elif ctx.NOTEQUAL(): return BinExpr(ctx.NOTEQUAL().getText(),left, right)
            elif ctx.LESS(): return BinExpr(ctx.LESS().getText(),left, right)
            elif ctx.LESSEQUAL(): return BinExpr(ctx.LESSEQUAL().getText(),left, right)
            elif ctx.GREATER(): return BinExpr(ctx.GREATER().getText(),left, right)
            elif ctx.GREATEREQUAL(): return BinExpr(ctx.GREATEREQUAL().getText(),left, right)
        return self.visit(ctx.expr2(0))
    # expr2: expr2 (AND | OR) expr3 | expr3;
    def visitExpr2(self, ctx: MT22Parser.Expr2Context):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.expr2())
            right = self.visit(ctx.expr3())
            if ctx.AND(): return BinExpr(ctx.AND().getText(),left, right)
            elif ctx.OR(): return BinExpr(ctx.OR().getText(),left, right)
        return self.visit(ctx.expr3())
    # expr3: expr3 ( PLUS | MINUS) expr4 | expr4;
    def visitExpr3(self, ctx: MT22Parser.Expr3Context):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.expr3())
            right = self.visit(ctx.expr4())
            if ctx.PLUS(): return BinExpr(ctx.PLUS().getText(),left, right)
            elif ctx.MINUS(): return BinExpr(ctx.MINUS().getText(),left, right)
        return self.visit(ctx.expr4())
    # expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;
    def visitExpr4(self, ctx: MT22Parser.Expr4Context):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.expr4())
            right = self.visit(ctx.expr5())
            if ctx.MUL(): return BinExpr(ctx.MUL().getText(),left, right)
            elif ctx.DIV(): return BinExpr(ctx.DIV().getText(),left, right)
            elif ctx.MOD(): return BinExpr(ctx.MOD().getText(),left, right)
        return self.visit(ctx.expr5())
    # expr5: NOT expr5 | expr6;
    def visitExpr5(self, ctx: MT22Parser.Expr5Context):
        if ctx.NOT():
            op = ctx.NOT().getText()
            exp = self.visit(ctx.expr5())
            return UnExpr(op, exp)
        return self.visit(ctx.expr6())
    # expr6: MINUS expr6 | expr7;
    def visitExpr6(self, ctx: MT22Parser.Expr6Context):
        if ctx.MINUS():
            op = ctx.MINUS().getText()
            exp = self.visit(ctx.expr6())
            return UnExpr(op, exp)
        return self.visit(ctx.expr7())
    # expr7: IDENTIFIERS LSQUAREBR exprprime RSQUAREBR | expr8;
    def visitExpr7(self, ctx: MT22Parser.Expr7Context):
        if ctx.getChildCount()==1: return self.visit(ctx.expr8())
        name = ctx.IDENTIFIERS().getText()
        exprs = self.visit(ctx.exprprime())
        return ArrayCell(name, exprs)
    # expr8: INTLIT | FLOATLIT | STRINGLIT | BOOLEANLIT | IDENTIFIER | callexpr | subexpr | arraylit;
    def visitExpr8(self, ctx: MT22Parser.Expr8Context):
        if ctx.INTLIT(): return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT(): return FloatLit(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT(): return StringLit(ctx.STRINGLIT().getText())
        elif ctx.BOOLEANLIT(): return BooleanLit(ctx.BOOLEANLIT().getText() == 'true')
        elif ctx.IDENTIFIERS(): return Id(ctx.IDENTIFIERS().getText())
        elif ctx.callexpr(): return self.visit(ctx.callexpr())
        elif ctx.subexpr(): return self.visit(ctx.subexpr())
        elif ctx.arraylit(): return self.visit(ctx.arraylit())
    # callexpr: IDENTIFIERS LROUNDBR exprlist RROUNDBR;
    def visitCallexpr(self, ctx: MT22Parser.CallexprContext):
        name = ctx.IDENTIFIERS().getText()
        exprs = self.visit(ctx.exprlist())
        return FuncCall(name, exprs)
    # subexpr: LROUNDBR expr RROUNDBR;
    def visitSubexpr(self, ctx: MT22Parser.SubexprContext):
        return self.visit(ctx.expr())
    # scalavar: IDENTIFIERS | idxop;
    def visitScalavar(self, ctx: MT22Parser.ScalavarContext):
        if ctx.IDENTIFIERS():
            return Id(ctx.IDENTIFIERS().getText())
        return self.visit(ctx.idxop())
