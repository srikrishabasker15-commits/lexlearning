%{
#include <stdio.h>
#include <stdlib.h>

int yylex(void);
void yyerror(const char *s);
%}

/* Token declarations (must match lexer.l) */
%token IF ELSE ID NUM PLUS SEMI LPAREN RPAREN

%%

program:
        program statement
        | statement
        ;

statement:
        ID PLUS NUM SEMI
        | IF LPAREN ID RPAREN statement
        ;

%%

/* Main function */
int main() {
    printf("Enter input:\n");
    if (yyparse() == 0) {
        printf("Syntax is VALID ✅\n");
    }
    return 0;
}

/* Error handling */
void yyerror(const char *s) {
    printf("Syntax Error ❌\n");
}
