import re
from io import StringIO

import antlr4
from antlr4 import (CommonTokenStream, InputStream, ParserRuleContext,
                    ParseTreeWalker)

from Java8Lexer import Java8Lexer
from Java8Parser import Java8Parser
from Java8ParserListener import Java8ParserListener


class MyListener(Java8ParserListener):

    def __init__(self, output_stream, method_map_dict, package_map_dict):
        self.output_stream = output_stream
        self.method_map_dict = method_map_dict
        self.package_map_dict = package_map_dict
        self.object_dict = {}

    def enterImportDeclaration(self, ctx: Java8Parser.ImportDeclarationContext):
        # get package name and replace it
        package_body = ctx.getText()
        package_name = ctx.singleTypeImportDeclaration().typeName().getText()
        new_package_name = self.package_map_dict.get(package_name, package_name)
        package_body = re.sub(rf"{package_name}\b", new_package_name, package_body)
        self.output_stream.write(package_body)

    def enterClassDeclaration(self, ctx: Java8Parser.ClassDeclarationContext):
        # get class name
        self.class_name = ctx.getChild(0).Identifier().getText()
        self.object_dict[self.class_name] = []

    def enterMethodHeader(self, ctx: Java8Parser.MethodHeaderContext):
        # get method name
        for i in range(ctx.getChildCount()):
            if isinstance(ctx.getChild(i), Java8Parser.MethodDeclaratorContext):
                method_name = ctx.getChild(i).Identifier().getText()
                self.object_dict[self.class_name].append(method_name)

    def enterMethodDeclaration(self, ctx: Java8Parser.MethodDeclarationContext):
        # rewrite method name and package name
        for i in range(ctx.methodHeader().getChildCount()):
            child = ctx.methodHeader().getChild(i)
            if isinstance(child, Java8Parser.MethodDeclaratorContext):
                method_name = child.Identifier().getText()
                new_method_name = self.method_map_dict.get(method_name, method_name)
                self.output_stream.write(new_method_name)

                # Write method parameters
                method_body = ctx.methodBody().getText()
                for key, value in self.method_map_dict.items():
                    method_body = re.sub(rf"\b{key}\b", value, method_body)

                # Write imported package(need customized)
                for key, value in self.package_map_dict.items():
                    key = key.split('.')[-1]
                    value = value.split('.')[-1]
                    method_body = re.sub(rf"\b{key}\b", value, method_body)

                # Write method body
                self.output_stream.write(method_body)


if __name__ == "__main__":
    # 建立一個新的 ANTLR 解析器
    file_name = "test.java"
    lexer = Java8Lexer(InputStream(open(file_name, "r", encoding="utf-8").read()))
    tokens = CommonTokenStream(lexer)
    parser = Java8Parser(tokens)

    # 解析 Java 程式碼
    tree = parser.compilationUnit()

    # Replace function name and generate new Java content
    method_map_dict = {'sayHello': 'sayHi'}
    package_map_dict = {'java.util.Arrays': 'java.util.List', 'java.util.HashMap': 'java.util.Map'}
    output_stream = StringIO()

    # 建立一個新的 MyListener 物件
    listener = MyListener(output_stream, method_map_dict, package_map_dict)

    # 遍歷 parse tree
    walker = ParseTreeWalker()
    walker.DEFAULT.walk(listener, tree)

    # 列印出所有 function name
    print("Functions: ", listener.object_dict)

    # Save the modified content to a new .java file
    new_java_content = listener.output_stream.getvalue()
    with open("ModifiedJavaFile.java", "w") as f:
        f.write(new_java_content)
