
/* A Bison parser, made by GNU Bison 2.4.1.  */

/* Skeleton interface for Bison's Yacc-like parsers in C
   
      Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.
   
   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */


/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     INSTANCE = 258,
     OF = 259,
     ENDOFFILE = 260,
     OPENBRACKET = 261,
     CLOSEBRACKET = 262,
     COMMA = 263,
     CLASS = 264,
     PROPERTYNAME = 265,
     STRING = 266,
     BOOLEAN = 267,
     INTEGER = 268,
     CIMNULL = 269
   };
#endif
/* Tokens.  */
#define INSTANCE 258
#define OF 259
#define ENDOFFILE 260
#define OPENBRACKET 261
#define CLOSEBRACKET 262
#define COMMA 263
#define CLASS 264
#define PROPERTYNAME 265
#define STRING 266
#define BOOLEAN 267
#define INTEGER 268
#define CIMNULL 269




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE
{

/* Line 1676 of yacc.c  */
#line 53 "eo_util_parser.y"

   /* Note - we override the CIM definition of string to make this data type
      easier to handle in the lexer/parser. Instead implemented as simple text string. */
   char *               string;
   CMPIBoolean          boolean;
   CMPISint64           sint64;



/* Line 1676 of yacc.c  */
#line 90 "eo_util_parser.h"
} YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif

extern YYSTYPE eo_parse_lval;


