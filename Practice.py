{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "5dd2d42d",
   "metadata": {},
   "source": [
    "# Python Basics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e3606cc1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello world\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello world\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e887730d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello \n",
      " world\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello \\n world\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3c0926a3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello \" world\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello \\\" world\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "8f3a6fca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "prajna shetty\n",
      "PRAJNA SHETTY\n",
      "False\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "word = \"Prajna Shetty\"\n",
    "print(word.lower())\n",
    "print(word.upper())\n",
    "print(word.islower())\n",
    "print(word.isupper())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "eb1079ad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "13\n"
     ]
    }
   ],
   "source": [
    "print(len(word))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "8d1c9ff0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "word P\n"
     ]
    }
   ],
   "source": [
    "print(\"word \" + word[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "347bfe69",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n"
     ]
    }
   ],
   "source": [
    "print(word.index(\"S\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "0fddc9ef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pratheek Shetty\n"
     ]
    }
   ],
   "source": [
    "print(word.replace(\"Prajna\",\"Pratheek\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "466606b6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "num = 3\n",
    "print(str(num))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b50ec288",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n"
     ]
    }
   ],
   "source": [
    "dig = -7\n",
    "print(abs(dig))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "0e801f10",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "49\n"
     ]
    }
   ],
   "source": [
    "print(pow(dig,2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "4353e229",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "-7\n"
     ]
    }
   ],
   "source": [
    "print(max(dig,num))\n",
    "print(min(dig,num))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "d766e7d4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "print(round(3.7))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "662f6240",
   "metadata": {},
   "source": [
    "# Math functions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "451e18a9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "4\n",
      "1.9235384061671346\n"
     ]
    }
   ],
   "source": [
    "from math import *\n",
    "\n",
    "print(floor(3.7))\n",
    "print(ceil(3.7))\n",
    "print(sqrt(3.7))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "50bf5b81",
   "metadata": {},
   "source": [
    "# Input"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "65eacf23",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your name: Sai\n",
      "Sai\n"
     ]
    }
   ],
   "source": [
    "name = input(\"Enter your name: \")\n",
    "print(name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "b54d89b5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number 1\n",
      "Enter a number 2\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "a = input(\"Enter a number \")\n",
    "b = input(\"Enter a number \")\n",
    "print(int(a)+int(b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "087c3624",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number 3.9\n",
      "Enter a number 9.0\n",
      "12.9\n"
     ]
    }
   ],
   "source": [
    "a = input(\"Enter a number \")\n",
    "b = input(\"Enter a number \")\n",
    "print(float(a)+float(b))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "143c1954",
   "metadata": {},
   "source": [
    "# Arrays"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "1ae8e8d5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['lmh', 'ghi']\n"
     ]
    }
   ],
   "source": [
    "peep = [\"abc\",\"lmh\",\"ghi\",\"yuo\"]\n",
    "print(peep[1:3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "077d8f27",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['def', 'ghi', 'jkl']\n"
     ]
    }
   ],
   "source": [
    "print(peep[1:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "3f9b797f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['abc', 'def', 'ghi']\n"
     ]
    }
   ],
   "source": [
    "print(peep[:3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "ed12e739",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['abc', 'def', 'ghi', 'jkl', 1, 2, 3]\n"
     ]
    }
   ],
   "source": [
    "nums = [1,2,3]\n",
    "peep.extend(nums)\n",
    "print(peep)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "4af11532",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['abc', 'def', 'ghi', 'jkl', 'mno']\n"
     ]
    }
   ],
   "source": [
    "peep.append(\"mno\")\n",
    "print(peep)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "1a37bc8e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['abc', 'new', 'def', 'ghi', 'jkl', 'mno']\n"
     ]
    }
   ],
   "source": [
    "peep.insert(1, \"new\")\n",
    "print(peep)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "28d44b9c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['abc', 'new', 'def', 'ghi', 'jkl']\n"
     ]
    }
   ],
   "source": [
    "peep.remove(\"mno\")\n",
    "print(peep)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "c6df5d39",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['abc', 'new', 'def', 'ghi']\n"
     ]
    }
   ],
   "source": [
    "peep.pop()\n",
    "print(peep)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "3b855ce3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[]\n"
     ]
    }
   ],
   "source": [
    "peep.clear()\n",
    "print(peep)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "beed89f1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n"
     ]
    }
   ],
   "source": [
    "print(peep.index(\"abc\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "d070a68a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "print(peep.count(\"abc\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "f75fc0a5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['abc', 'ghi', 'lmh', 'yuo']\n"
     ]
    }
   ],
   "source": [
    "peep.sort()\n",
    "print(peep)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "983ffc8e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['yuo', 'lmh', 'ghi', 'abc']\n"
     ]
    }
   ],
   "source": [
    "peep.reverse()\n",
    "print(peep)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "124a5ec5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['yuo', 'lmh', 'ghi', 'abc']\n"
     ]
    }
   ],
   "source": [
    "peep2 = peep.copy()\n",
    "print(peep2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "350becf5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['abc', 'lmh', 'ghi', 'yuo']\n"
     ]
    }
   ],
   "source": [
    "tuple = [\"abc\",\"lmh\",\"ghi\",\"yuo\"]\n",
    "print(tuple)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "5ffe8bc8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('abc', 'lmh'), ('ghi', 'yuo')]\n"
     ]
    }
   ],
   "source": [
    "tuplelist = [(\"abc\",\"lmh\"),(\"ghi\",\"yuo\")]\n",
    "print(tuplelist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "f2bf8b29",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hi\n"
     ]
    }
   ],
   "source": [
    "def first_function():\n",
    "    print(\"Hi\")\n",
    "first_function()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d3fb9842",
   "metadata": {},
   "source": [
    "# If, for, dictonaries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "5299d181",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Always\n"
     ]
    }
   ],
   "source": [
    "if 1<2 or 2>1:\n",
    "    print(\"Always\")\n",
    "elif 1<3 and not(3>1):\n",
    "    print(\"Never\")\n",
    "else:\n",
    "    print(\"no\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "28523764",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'jan': '1', 'feb': '2', 'mar': '3'}\n"
     ]
    }
   ],
   "source": [
    "dictonaries = {\n",
    "    \"jan\": \"1\",\n",
    "    \"feb\": \"2\",\n",
    "    \"mar\": \"3\",\n",
    "}\n",
    "print(dictonaries)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "0f6e265e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "print(dictonaries[\"feb\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "b9cc438d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "print(dictonaries.get(\"feb\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "2de10a22",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "print(dictonaries.get(\"Apr\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "911f7991",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Not present\n"
     ]
    }
   ],
   "source": [
    "print(dictonaries.get(\"Apr\", \"Not present\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "96cbd86e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "P\n",
      "r\n",
      "a\n",
      "j\n",
      "n\n",
      "a\n",
      " \n",
      "S\n",
      "h\n",
      "e\n",
      "t\n",
      "t\n",
      "y\n"
     ]
    }
   ],
   "source": [
    "for name in \"Prajna Shetty\":\n",
    "    print(name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7b3ee09f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n"
     ]
    }
   ],
   "source": [
    "for i in range(10):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9f46bae2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n",
      "11\n"
     ]
    }
   ],
   "source": [
    "for i in range(len(\"PrajnaShetty\")):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c4d4e09b",
   "metadata": {},
   "source": [
    "# try except"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b53dd0a2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number: iop\n",
      "Exception occured\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    num = int(input(\"Enter the number: \"))\n",
    "    print(num)\n",
    "except:\n",
    "    print(\"Exception occured\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "84ef2c79",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number: 0\n",
      "Cant divide by zero\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    num = int(input(\"Enter the number: \"))\n",
    "    print(2/num)\n",
    "except ZeroDivisionError:\n",
    "    print(\"Cant divide by zero\")\n",
    "except ValueError:\n",
    "    print(\"Invalid value\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b9131311",
   "metadata": {},
   "source": [
    "# Files"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "3efd9004",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "new line\n"
     ]
    }
   ],
   "source": [
    "#Reading files\n",
    "file = open(\"cinderella.txt\", \"r\")\n",
    "print(file.readable())\n",
    "print(file.read())\n",
    "file.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "cf5fa264",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "#Writing to files\n",
    "file = open(\"cinderella.txt\", \"w\")\n",
    "print(file.readable())\n",
    "file.write(\"new line\")\n",
    "file.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "10712f1f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "#Appending files\n",
    "file = open(\"cinderella.txt\", \"a\")\n",
    "print(file.readable())\n",
    "file.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "fa8679b5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "uiiui\n",
      "\n"
     ]
    }
   ],
   "source": [
    "#Reading and Writing files\n",
    "file = open(\"cinderella.txt\", \"r+\")\n",
    "print(file.readable())\n",
    "print(file.readline())\n",
    "file.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "233e2c06",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['uiiui\\n', 'ioiop\\n', 'oippop[o\\n', 'nljbkjb\\n', '\\n', '\\n', 'kjjhb\\n', 'nmmmmmmmmmmmmjbjnm ']\n"
     ]
    }
   ],
   "source": [
    "#Puts in a List\n",
    "file = open(\"cinderella.txt\", \"r\")\n",
    "print(file.readlines())\n",
    "file.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "23cd3648",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ioiop\n",
      "\n"
     ]
    }
   ],
   "source": [
    "file = open(\"cinderella.txt\", \"r\")\n",
    "print(file.readlines()[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "3ba97603",
   "metadata": {},
   "outputs": [],
   "source": [
    "for j in file.readlines():\n",
    "    print(j)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "be6262ec",
   "metadata": {},
   "source": [
    "# Numpy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "a41c62e7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "a  = np.array([1,2,3])\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "d66bedbd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3]\n",
      " [3 4 5]]\n"
     ]
    }
   ],
   "source": [
    "b  = np.array([[1,2,3], [3,4,5]])\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "9dd4d88e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.ndim"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "423aeb37",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.ndim"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "0f84cc13",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3,)"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "f60709cf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2, 3)"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "de1427da",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('int32')"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.dtype"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "1b3fcb05",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('int16')"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c  = np.array([[1,2,3], [3,4,5]], dtype='int16')\n",
    "c.dtype"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "0bba6225",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.itemsize"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "1d557497",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c.itemsize"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "3ce0fba5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "82344786",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "12"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.nbytes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "d4234209",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "12"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c.nbytes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "1864b5e1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[3, 5, 6, 7],\n",
       "       [6, 2, 3, 5]])"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x= np.array([[1,2,3,4],[3,5,6,7],[6,2,3,5]])\n",
    "x[1:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "984797d5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3, 4],\n",
       "       [3, 5, 6, 7],\n",
       "       [6, 2, 3, 5]])"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x[:3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "7b9d7718",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[6, 2, 3, 5]])"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x[2:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "10d66eef",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 3, 4])"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x[0, :]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "d9550e81",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([3, 6, 3])"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x[: , 2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "f77a4787",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([2])"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Skip by 2 from 1-3th col 0 row\n",
    "x[0,1:3:2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "24d2cf3b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[  1,   2,   3,   4],\n",
       "       [  3,   5,   6, 100],\n",
       "       [  6,   2,   3,   5]])"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x[1,3] = 100\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "4963c270",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[1, 2, 3, 4],\n",
       "        [3, 5, 6, 7],\n",
       "        [6, 2, 3, 5]],\n",
       "\n",
       "       [[1, 2, 3, 4],\n",
       "        [3, 5, 6, 7],\n",
       "        [6, 2, 3, 5]]])"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y = np.array([[[1,2,3,4],[3,5,6,7],[6,2,3,5]],[[1,2,3,4],[3,5,6,7],[6,2,3,5]]])\n",
    "y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "b3c402a2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[1, 2, 3, 4],\n",
       "        [5, 5, 5, 5],\n",
       "        [6, 2, 3, 5]],\n",
       "\n",
       "       [[1, 2, 3, 4],\n",
       "        [6, 6, 6, 6],\n",
       "        [6, 2, 3, 5]]])"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y[:,1,:] = [[5,5,5,5],[6,6,6,6]]\n",
    "y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "a38fd3f4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[6, 2, 3, 5],\n",
       "       [6, 2, 3, 5]])"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y[:,2,:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "26995bb1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0., 0., 0., 0., 0.])"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.zeros(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "21afab2f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[0., 0.],\n",
       "        [0., 0.],\n",
       "        [0., 0.]],\n",
       "\n",
       "       [[0., 0.],\n",
       "        [0., 0.],\n",
       "        [0., 0.]]])"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.zeros(((2,3,2)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "47a73941",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[1., 1.],\n",
       "        [1., 1.],\n",
       "        [1., 1.]],\n",
       "\n",
       "       [[1., 1.],\n",
       "        [1., 1.],\n",
       "        [1., 1.]]])"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.ones((2,3,2), dtype='int32')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "7fc0c13e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[99, 99],\n",
       "       [99, 99]])"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.full((2,2),99)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "ee52ff60",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[4, 4, 4, 4],\n",
       "        [4, 4, 4, 4],\n",
       "        [4, 4, 4, 4]],\n",
       "\n",
       "       [[4, 4, 4, 4],\n",
       "        [4, 4, 4, 4],\n",
       "        [4, 4, 4, 4]]])"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.full_like(y,4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "1f298e2e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[0.59464779, 0.66558055, 0.99493082],\n",
       "        [0.19439909, 0.45934154, 0.60439465]],\n",
       "\n",
       "       [[0.43642857, 0.04569863, 0.87243586],\n",
       "        [0.70698631, 0.7771461 , 0.97506303]],\n",
       "\n",
       "       [[0.45153203, 0.37180311, 0.04171573],\n",
       "        [0.80519819, 0.73697785, 0.0953708 ]],\n",
       "\n",
       "       [[0.41907435, 0.46228584, 0.1285454 ],\n",
       "        [0.4633853 , 0.95595397, 0.55575657]]])"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.random.rand(4,2,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "a339bfd9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1., 1., 1., 1., 1.],\n",
       "       [1., 0., 0., 0., 1.],\n",
       "       [1., 0., 0., 0., 1.],\n",
       "       [1., 0., 0., 0., 1.],\n",
       "       [1., 1., 1., 1., 1.]])"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "o = np.ones((5,5))\n",
    "o[1:-1,1:-1] = 0\n",
    "o"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "8b03bd07",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 3])"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b = a.copy()\n",
    "b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "a7ffc4eb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([2, 4, 6])"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b*2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "59c03fc5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([2, 4, 6])"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a+b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "260446b8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0.54030231, -0.41614684, -0.9899925 ])"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.cos(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "0d94dce1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[25, 31],\n",
       "       [45, 57]])"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c  = np.array([[1,2], [3,4],[6,7]])\n",
    "np.matmul(b,c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d67865e8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Load data from file\n",
    "filedata = np.genfromtxt('data.txt',delimiters=',')\n",
    "filedata[filedata>50 ]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c423c837",
   "metadata": {},
   "source": [
    "# Pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4af4d6ca",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "02ea692f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        last                                       first gender   age  class  \\\n",
      "0     Braund                             Mr. Owen Harris      M  22.0      3   \n",
      "1    Cumings  Mrs. John Bradley (Florence Briggs Thayer)      F  38.0      1   \n",
      "2  Heikkinen                                  Miss Laina      F  26.0      3   \n",
      "3   Futrelle          Mrs. Jacques Heath (Lily May Peel)      F  35.0      1   \n",
      "4      Allen                           Mr. William Henry      M  35.0      3   \n",
      "\n",
      "      fare     embarked survived  \n",
      "0   7.2500  Southampton       no  \n",
      "1  71.2833    Cherbourg      yes  \n",
      "2   7.9250  Southampton      yes  \n",
      "3  53.1000  Southampton      yes  \n",
      "4   8.0500  Southampton       no  \n"
     ]
    }
   ],
   "source": [
    "df = pd.read_csv(\"Titanic.csv\")\n",
    "print(df.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "68fb08cd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['last', 'first', 'gender', 'age', 'class', 'fare', 'embarked',\n",
      "       'survived'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "print(df.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ea63981b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0         Braund\n",
       "1        Cumings\n",
       "2      Heikkinen\n",
       "3       Futrelle\n",
       "4          Allen\n",
       "         ...    \n",
       "886     Montvila\n",
       "887       Graham\n",
       "888     Johnston\n",
       "889         Behr\n",
       "890       Dooley\n",
       "Name: last, Length: 891, dtype: object"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"last\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "dd215457",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<bound method NDFrame.last of           last                                       first gender   age  \\\n",
       "0       Braund                             Mr. Owen Harris      M  22.0   \n",
       "1      Cumings  Mrs. John Bradley (Florence Briggs Thayer)      F  38.0   \n",
       "2    Heikkinen                                  Miss Laina      F  26.0   \n",
       "3     Futrelle          Mrs. Jacques Heath (Lily May Peel)      F  35.0   \n",
       "4        Allen                           Mr. William Henry      M  35.0   \n",
       "..         ...                                         ...    ...   ...   \n",
       "886   Montvila                                 Rev. Juozas      M  27.0   \n",
       "887     Graham                         Miss Margaret Edith      F  19.0   \n",
       "888   Johnston               Miss Catherine Helen \"Carrie\"      F   NaN   \n",
       "889       Behr                             Mr. Karl Howell      M  26.0   \n",
       "890     Dooley                                 Mr. Patrick      M  32.0   \n",
       "\n",
       "     class     fare     embarked survived  \n",
       "0        3   7.2500  Southampton       no  \n",
       "1        1  71.2833    Cherbourg      yes  \n",
       "2        3   7.9250  Southampton      yes  \n",
       "3        1  53.1000  Southampton      yes  \n",
       "4        3   8.0500  Southampton       no  \n",
       "..     ...      ...          ...      ...  \n",
       "886      2  13.0000  Southampton       no  \n",
       "887      1  30.0000  Southampton      yes  \n",
       "888      3  23.4500  Southampton       no  \n",
       "889      1  30.0000    Cherbourg      yes  \n",
       "890      3   7.7500   Queenstown       no  \n",
       "\n",
       "[891 rows x 8 columns]>"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.last"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "b1695a73",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>last</th>\n",
       "      <th>first</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Braund</td>\n",
       "      <td>Mr. Owen Harris</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Cumings</td>\n",
       "      <td>Mrs. John Bradley (Florence Briggs Thayer)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Heikkinen</td>\n",
       "      <td>Miss Laina</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Futrelle</td>\n",
       "      <td>Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Allen</td>\n",
       "      <td>Mr. William Henry</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>886</th>\n",
       "      <td>Montvila</td>\n",
       "      <td>Rev. Juozas</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>887</th>\n",
       "      <td>Graham</td>\n",
       "      <td>Miss Margaret Edith</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>Johnston</td>\n",
       "      <td>Miss Catherine Helen \"Carrie\"</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>Behr</td>\n",
       "      <td>Mr. Karl Howell</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>Dooley</td>\n",
       "      <td>Mr. Patrick</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>891 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "          last                                       first\n",
       "0       Braund                             Mr. Owen Harris\n",
       "1      Cumings  Mrs. John Bradley (Florence Briggs Thayer)\n",
       "2    Heikkinen                                  Miss Laina\n",
       "3     Futrelle          Mrs. Jacques Heath (Lily May Peel)\n",
       "4        Allen                           Mr. William Henry\n",
       "..         ...                                         ...\n",
       "886   Montvila                                 Rev. Juozas\n",
       "887     Graham                         Miss Margaret Edith\n",
       "888   Johnston               Miss Catherine Helen \"Carrie\"\n",
       "889       Behr                             Mr. Karl Howell\n",
       "890     Dooley                                 Mr. Patrick\n",
       "\n",
       "[891 rows x 2 columns]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[['last','first']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "ca92e642",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>first</th>\n",
       "      <th>gender</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mrs. John Bradley (Florence Briggs Thayer)</td>\n",
       "      <td>F</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Miss Laina</td>\n",
       "      <td>F</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>F</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                        first gender\n",
       "1  Mrs. John Bradley (Florence Briggs Thayer)      F\n",
       "2                                  Miss Laina      F\n",
       "3          Mrs. Jacques Heath (Lily May Peel)      F"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.iloc[1:4, 1:3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "8baf2b58",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Miss Laina'"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.iloc[2,1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "d83aa465",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 Braund\n",
      "1 Cumings\n",
      "2 Heikkinen\n",
      "3 Futrelle\n",
      "4 Allen\n",
      "5 Moran\n",
      "6 McCarthy\n",
      "7 Palsson\n",
      "8 Johnson\n",
      "9 Nasser\n",
      "10 Sandstrom\n",
      "11 Bonnell\n",
      "12 Saundercock\n",
      "13 Andersson\n",
      "14 Vestrom\n",
      "15 Hewlett\n",
      "16 Rice\n",
      "17 Williams\n",
      "18 Vander Planke\n",
      "19 Masselmani\n",
      "20 Fynney\n",
      "21 Beesley\n",
      "22 McGowan\n",
      "23 Sloper\n",
      "24 Palsson\n",
      "25 Asplund\n",
      "26 Emir\n",
      "27 Fortune\n",
      "28 O'Dwyer\n",
      "29 Todoroff\n",
      "30 Uruchurtu\n",
      "31 Spencer\n",
      "32 Glynn\n",
      "33 Wheadon\n",
      "34 Meyer\n",
      "35 Holverson\n",
      "36 Mamee\n",
      "37 Cann\n",
      "38 Vander Planke\n",
      "39 Nicola-Yarred\n",
      "40 Ahlin\n",
      "41 Turpin\n",
      "42 Kraeff\n",
      "43 Laroche\n",
      "44 Devaney\n",
      "45 Rogers\n",
      "46 Lennon\n",
      "47 O'Driscoll\n",
      "48 Samaan\n",
      "49 Arnold-Franchi\n",
      "50 Panula\n",
      "51 Nosworthy\n",
      "52 Harper\n",
      "53 Faunthorpe\n",
      "54 Ostby\n",
      "55 Woolner\n",
      "56 Rugg\n",
      "57 Novel\n",
      "58 West\n",
      "59 Goodwin\n",
      "60 Sirayanian\n",
      "61 Icard\n",
      "62 Harris\n",
      "63 Skoog\n",
      "64 Stewart\n",
      "65 Moubarek\n",
      "66 Nye\n",
      "67 Crease\n",
      "68 Andersson\n",
      "69 Kink\n",
      "70 Jenkin\n",
      "71 Goodwin\n",
      "72 Hood\n",
      "73 Chronopoulos\n",
      "74 Bing\n",
      "75 Moen\n",
      "76 Staneff\n",
      "77 Moutal\n",
      "78 Caldwell\n",
      "79 Dowdell\n",
      "80 Waelens\n",
      "81 Sheerlinck\n",
      "82 McDermott\n",
      "83 Carrau\n",
      "84 Ilett\n",
      "85 Backstrom\n",
      "86 Ford\n",
      "87 Slocovski\n",
      "88 Fortune\n",
      "89 Celotti\n",
      "90 Christmann\n",
      "91 Andreasson\n",
      "92 Chaffee\n",
      "93 Dean\n",
      "94 Coxon\n",
      "95 Shorney\n",
      "96 Goldschmidt\n",
      "97 Greenfield\n",
      "98 Doling\n",
      "99 Kantor\n",
      "100 Petranec\n",
      "101 Petroff\n",
      "102 White\n",
      "103 Johansson\n",
      "104 Gustafsson\n",
      "105 Mionoff\n",
      "106 Salkjelsvik\n",
      "107 Moss\n",
      "108 Rekic\n",
      "109 Moran\n",
      "110 Porter\n",
      "111 Zabour\n",
      "112 Barton\n",
      "113 Jussila\n",
      "114 Attalah\n",
      "115 Pekoniemi\n",
      "116 Connors\n",
      "117 Turpin\n",
      "118 Baxter\n",
      "119 Andersson\n",
      "120 Hickman\n",
      "121 Moore\n",
      "122 Nasser\n",
      "123 Webber\n",
      "124 White\n",
      "125 Nicola-Yarred\n",
      "126 McMahon\n",
      "127 Madsen\n",
      "128 Peter\n",
      "129 Ekstrom\n",
      "130 Drazenoic\n",
      "131 Coelho\n",
      "132 Robins\n",
      "133 Weisz\n",
      "134 Sobey\n",
      "135 Richard\n",
      "136 Newsom\n",
      "137 Futrelle\n",
      "138 Osen\n",
      "139 Giglio\n",
      "140 Boulos\n",
      "141 Nysten\n",
      "142 Hakkarainen\n",
      "143 Burke\n",
      "144 Andrew\n",
      "145 Nicholls\n",
      "146 Andersson\n",
      "147 Ford\n",
      "148 Navratil\n",
      "149 Byles\n",
      "150 Bateman\n",
      "151 Pears\n",
      "152 Meo\n",
      "153 van Billiard\n",
      "154 Olsen\n",
      "155 Williams\n",
      "156 Gilnagh\n",
      "157 Corn\n",
      "158 Smiljanic\n",
      "159 Sage\n",
      "160 Cribb\n",
      "161 Watt\n",
      "162 Bengtsson\n",
      "163 Calic\n",
      "164 Panula\n",
      "165 Goldsmith\n",
      "166 Chibnall\n",
      "167 Skoog\n",
      "168 Baumann\n",
      "169 Ling\n",
      "170 Van der hoef\n",
      "171 Rice\n",
      "172 Johnson\n",
      "173 Sivola\n",
      "174 Smith\n",
      "175 Klasen\n",
      "176 Lefebre\n",
      "177 Isham\n",
      "178 Hale\n",
      "179 Leonard\n",
      "180 Sage\n",
      "181 Pernot\n",
      "182 Asplund\n",
      "183 Becker\n",
      "184 Kink-Heilmann\n",
      "185 Rood\n",
      "186 O'Brien\n",
      "187 Romaine\n",
      "188 Bourke\n",
      "189 Turcin\n",
      "190 Pinsky\n",
      "191 Carbines\n",
      "192 Andersen-Jensen\n",
      "193 Navratil\n",
      "194 Brown\n",
      "195 Lurette\n",
      "196 Mernagh\n",
      "197 Olsen\n",
      "198 Madigan\n",
      "199 Yrois\n",
      "200 Vande Walle\n",
      "201 Sage\n",
      "202 Johanson\n",
      "203 Youseff\n",
      "204 Cohen\n",
      "205 Strom\n",
      "206 Backstrom\n",
      "207 Albimona\n",
      "208 Carr\n",
      "209 Blank\n",
      "210 Ali\n",
      "211 Cameron\n",
      "212 Perkin\n",
      "213 Givard\n",
      "214 Kiernan\n",
      "215 Newell\n",
      "216 Honkanen\n",
      "217 Jacobsohn\n",
      "218 Bazzani\n",
      "219 Harris\n",
      "220 Sunderland\n",
      "221 Bracken\n",
      "222 Green\n",
      "223 Nenkoff\n",
      "224 Hoyt\n",
      "225 Berglund\n",
      "226 Mellors\n",
      "227 Lovell\n",
      "228 Fahlstrom\n",
      "229 Lefebre\n",
      "230 Harris\n",
      "231 Larsson\n",
      "232 Sjostedt\n",
      "233 Asplund\n",
      "234 Leyson\n",
      "235 Harknett\n",
      "236 Hold\n",
      "237 Collyer\n",
      "238 Pengelly\n",
      "239 Hunt\n",
      "240 Zabour\n",
      "241 Murphy\n",
      "242 Coleridge\n",
      "243 Maenpaa\n",
      "244 Attalah\n",
      "245 Minahan\n",
      "246 Lindahl\n",
      "247 Hamalainen\n",
      "248 Beckwith\n",
      "249 Carter\n",
      "250 Reed\n",
      "251 Strom\n",
      "252 Stead\n",
      "253 Lobb\n",
      "254 Rosblom\n",
      "255 Touma\n",
      "256 Thorne\n",
      "257 Cherry\n",
      "258 Ward\n",
      "259 Parrish\n",
      "260 Smith\n",
      "261 Asplund\n",
      "262 Taussig\n",
      "263 Harrison\n",
      "264 Henry\n",
      "265 Reeves\n",
      "266 Panula\n",
      "267 Persson\n",
      "268 Graham\n",
      "269 Bissette\n",
      "270 Cairns\n",
      "271 Tornquist\n",
      "272 Mellinger\n",
      "273 Natsch\n",
      "274 Healy\n",
      "275 Andrews\n",
      "276 Lindblom\n",
      "277 Parkes\n",
      "278 Rice\n",
      "279 Abbott\n",
      "280 Duane\n",
      "281 Olsson\n",
      "282 de Pelsmaeker\n",
      "283 Dorking\n",
      "284 Smith\n",
      "285 Stankovic\n",
      "286 de Mulder\n",
      "287 Naidenoff\n",
      "288 Hosono\n",
      "289 Connolly\n",
      "290 Barber\n",
      "291 Bishop\n",
      "292 Levy\n",
      "293 Haas\n",
      "294 Mineff\n",
      "295 Lewy\n",
      "296 Hanna\n",
      "297 Allison\n",
      "298 Saalfeld\n",
      "299 Baxter\n",
      "300 Kelly\n",
      "301 McCoy\n",
      "302 Johnson\n",
      "303 Keane\n",
      "304 Williams\n",
      "305 Allison\n",
      "306 Fleming\n",
      "307 Penasco y Castellana\n",
      "308 Abelson\n",
      "309 Francatelli\n",
      "310 Hays\n",
      "311 Ryerson\n",
      "312 Lahtinen\n",
      "313 Hendekovic\n",
      "314 Hart\n",
      "315 Nilsson\n",
      "316 Kantor\n",
      "317 Moraweck\n",
      "318 Wick\n",
      "319 Spedden\n",
      "320 Dennis\n",
      "321 Danoff\n",
      "322 Slayter\n",
      "323 Caldwell\n",
      "324 Sage\n",
      "325 Young\n",
      "326 Nysveen\n",
      "327 Ball\n",
      "328 Goldsmith\n",
      "329 Hippach\n",
      "330 McCoy\n",
      "331 Partner\n",
      "332 Graham\n",
      "333 Vander Planke\n",
      "334 Frauenthal\n",
      "335 Denkoff\n",
      "336 Pears\n",
      "337 Burns\n",
      "338 Dahl\n",
      "339 Blackwell\n",
      "340 Navratil\n",
      "341 Fortune\n",
      "342 Collander\n",
      "343 Sedgwick\n",
      "344 Fox\n",
      "345 Brown\n",
      "346 Smith\n",
      "347 Davison\n",
      "348 Coutts\n",
      "349 Dimic\n",
      "350 Odahl\n",
      "351 Williams-Lambert\n",
      "352 Elias\n",
      "353 Arnold-Franchi\n",
      "354 Yousif\n",
      "355 Vanden Steen\n",
      "356 Bowerman\n",
      "357 Funk\n",
      "358 McGovern\n",
      "359 Mockler\n",
      "360 Skoog\n",
      "361 del Carlo\n",
      "362 Barbara\n",
      "363 Asim\n",
      "364 O'Brien\n",
      "365 Adahl\n",
      "366 Warren\n",
      "367 Moussa\n",
      "368 Jermyn\n",
      "369 Aubart\n",
      "370 Harder\n",
      "371 Wiklund\n",
      "372 Beavan\n",
      "373 Ringhini\n",
      "374 Palsson\n",
      "375 Meyer\n",
      "376 Landergren\n",
      "377 Widener\n",
      "378 Betros\n",
      "379 Gustafsson\n",
      "380 Bidois\n",
      "381 Nakid\n",
      "382 Tikkanen\n",
      "383 Holverson\n",
      "384 Plotcharsky\n",
      "385 Davies\n",
      "386 Goodwin\n",
      "387 Buss\n",
      "388 Sadlier\n",
      "389 Lehmann\n",
      "390 Carter\n",
      "391 Jansson\n",
      "392 Gustafsson\n",
      "393 Newell\n",
      "394 Sandstrom\n",
      "395 Johansson\n",
      "396 Olsson\n",
      "397 McKane\n",
      "398 Pain\n",
      "399 Trout\n",
      "400 Niskanen\n",
      "401 Adams\n",
      "402 Jussila\n",
      "403 Hakkarainen\n",
      "404 Oreskovic\n",
      "405 Gale\n",
      "406 Widegren\n",
      "407 Richards\n",
      "408 Birkeland\n",
      "409 Lefebre\n",
      "410 Sdycoff\n",
      "411 Hart\n",
      "412 Minahan\n",
      "413 Cunningham\n",
      "414 Sundman\n",
      "415 Meek\n",
      "416 Drew\n",
      "417 Silven\n",
      "418 Matthews\n",
      "419 Van Impe\n",
      "420 Gheorgheff\n",
      "421 Charters\n",
      "422 Zimmerman\n",
      "423 Danbom\n",
      "424 Rosblom\n",
      "425 Wiseman\n",
      "426 Clarke\n",
      "427 Phillips\n",
      "428 Flynn\n",
      "429 Pickard\n",
      "430 Bjornstrom-Steffansson\n",
      "431 Thorneycroft\n",
      "432 Louch\n",
      "433 Kallio\n",
      "434 Silvey\n",
      "435 Carter\n",
      "436 Ford\n",
      "437 Richards\n",
      "438 Fortune\n",
      "439 Kvillner\n",
      "440 Hart\n",
      "441 Hampe\n",
      "442 Petterson\n",
      "443 Reynaldo\n",
      "444 Johannesen-Bratthammer\n",
      "445 Dodge\n",
      "446 Mellinger\n",
      "447 Seward\n",
      "448 Baclini\n",
      "449 Peuchen\n",
      "450 West\n",
      "451 Hagland\n",
      "452 Foreman\n",
      "453 Goldenberg\n",
      "454 Peduzzi\n",
      "455 Jalsevac\n",
      "456 Millet\n",
      "457 Kenyon\n",
      "458 Toomey\n",
      "459 O'Connor\n",
      "460 Anderson\n",
      "461 Morley\n",
      "462 Gee\n",
      "463 Milling\n",
      "464 Maisner\n",
      "465 Goncalves\n",
      "466 Campbell\n",
      "467 Smart\n",
      "468 Scanlan\n",
      "469 Baclini\n",
      "470 Keefe\n",
      "471 Cacic\n",
      "472 West\n",
      "473 Jerwan\n",
      "474 Strandberg\n",
      "475 Clifford\n",
      "476 Renouf\n",
      "477 Braund\n",
      "478 Karlsson\n",
      "479 Hirvonen\n",
      "480 Goodwin\n",
      "481 Frost\n",
      "482 Rouse\n",
      "483 Turkula\n",
      "484 Bishop\n",
      "485 Lefebre\n",
      "486 Hoyt\n",
      "487 Kent\n",
      "488 Somerton\n",
      "489 Coutts\n",
      "490 Hagland\n",
      "491 Windelov\n",
      "492 Molson\n",
      "493 Artagaveytia\n",
      "494 Stanley\n",
      "495 Yousseff\n",
      "496 Eustis\n",
      "497 Shellard\n",
      "498 Allison\n",
      "499 Svensson\n",
      "500 Calic\n",
      "501 Canavan\n",
      "502 O'Sullivan\n",
      "503 Laitinen\n",
      "504 Maioni\n",
      "505 Penasco y Castellana\n",
      "506 Quick\n",
      "507 Bradley\n",
      "508 Olsen\n",
      "509 Lang\n",
      "510 Daly\n",
      "511 Webber\n",
      "512 McGough\n",
      "513 Rothschild\n",
      "514 Coleff\n",
      "515 Walker\n",
      "516 Lemore\n",
      "517 Ryan\n",
      "518 Angle\n",
      "519 Pavlovic\n",
      "520 Perreault\n",
      "521 Vovk\n",
      "522 Lahoud\n",
      "523 Hippach\n",
      "524 Kassem\n",
      "525 Farrell\n",
      "526 Ridsdale\n",
      "527 Farthing\n",
      "528 Salonen\n",
      "529 Hocking\n",
      "530 Quick\n",
      "531 Toufik\n",
      "532 Elias\n",
      "533 Peter\n",
      "534 Cacic\n",
      "535 Hart\n",
      "536 Butt\n",
      "537 LeRoy\n",
      "538 Risien\n",
      "539 Frolicher\n",
      "540 Crosby\n",
      "541 Andersson\n",
      "542 Andersson\n",
      "543 Beane\n",
      "544 Douglas\n",
      "545 Nicholson\n",
      "546 Beane\n",
      "547 Padro y Manent\n",
      "548 Goldsmith\n",
      "549 Davies\n",
      "550 Thayer\n",
      "551 Sharp\n",
      "552 O'Brien\n",
      "553 Leeni\n",
      "554 Ohman\n",
      "555 Wright\n",
      "556 Duff Gordon\n",
      "557 Robbins\n",
      "558 Taussig\n",
      "559 de Messemaeker\n",
      "560 Morrow\n",
      "561 Sivic\n",
      "562 Norman\n",
      "563 Simmons\n",
      "564 Meanwell\n",
      "565 Davies\n",
      "566 Stoytcheff\n",
      "567 Palsson\n",
      "568 Doharr\n",
      "569 Jonsson\n",
      "570 Harris\n",
      "571 Appleton\n",
      "572 Flynn\n",
      "573 Kelly\n",
      "574 Rush\n",
      "575 Patchett\n",
      "576 Garside\n",
      "577 Silvey\n",
      "578 Caram\n",
      "579 Jussila\n",
      "580 Christy\n",
      "581 Thayer\n",
      "582 Downton\n",
      "583 Ross\n",
      "584 Paulner\n",
      "585 Taussig\n",
      "586 Jarvis\n",
      "587 Frolicher-Stehli\n",
      "588 Gilinski\n",
      "589 Murdlin\n",
      "590 Rintamaki\n",
      "591 Stephenson\n",
      "592 Elsbury\n",
      "593 Bourke\n",
      "594 Chapman\n",
      "595 Van Impe\n",
      "596 Leitch\n",
      "597 Johnson\n",
      "598 Boulos\n",
      "599 Duff Gordon\n",
      "600 Jacobsohn\n",
      "601 Slabenoff\n",
      "602 Harrington\n",
      "603 Torber\n",
      "604 Homer\n",
      "605 Lindell\n",
      "606 Karaic\n",
      "607 Daniel\n",
      "608 Laroche\n",
      "609 Shutes\n",
      "610 Andersson\n",
      "611 Jardin\n",
      "612 Murphy\n",
      "613 Horgan\n",
      "614 Brocklebank\n",
      "615 Herman\n",
      "616 Danbom\n",
      "617 Lobb\n",
      "618 Becker\n",
      "619 Gavey\n",
      "620 Yasbeck\n",
      "621 Kimball\n",
      "622 Nakid\n",
      "623 Hansen\n",
      "624 Bowen\n",
      "625 Sutton\n",
      "626 Kirkland\n",
      "627 Longley\n",
      "628 Bostandyeff\n",
      "629 O'Connell\n",
      "630 Barkworth\n",
      "631 Lundahl\n",
      "632 Stahelin-Maeglin\n",
      "633 Parr\n",
      "634 Skoog\n",
      "635 Davis\n",
      "636 Leinonen\n",
      "637 Collyer\n",
      "638 Panula\n",
      "639 Thorneycroft\n",
      "640 Jensen\n",
      "641 Sagesser\n",
      "642 Skoog\n",
      "643 Foo\n",
      "644 Baclini\n",
      "645 Harper\n",
      "646 Cor\n",
      "647 Simonius-Blumer\n",
      "648 Willey\n",
      "649 Stanley\n",
      "650 Mitkoff\n",
      "651 Doling\n",
      "652 Kalvik\n",
      "653 O'Leary\n",
      "654 Hegarty\n",
      "655 Hickman\n",
      "656 Radeff\n",
      "657 Bourke\n",
      "658 Eitemiller\n",
      "659 Newell\n",
      "660 Frauenthal\n",
      "661 Badt\n",
      "662 Colley\n",
      "663 Coleff\n",
      "664 Lindqvist\n",
      "665 Hickman\n",
      "666 Butler\n",
      "667 Rommetvedt\n",
      "668 Cook\n",
      "669 Taylor\n",
      "670 Brown\n",
      "671 Davidson\n",
      "672 Mitchell\n",
      "673 Wilhelms\n",
      "674 Watson\n",
      "675 Edvardsson\n",
      "676 Sawyer\n",
      "677 Turja\n",
      "678 Goodwin\n",
      "679 Cardeza\n",
      "680 Peters\n",
      "681 Hassab\n",
      "682 Olsvigen\n",
      "683 Goodwin\n",
      "684 Brown\n",
      "685 Laroche\n",
      "686 Panula\n",
      "687 Dakic\n",
      "688 Fischer\n",
      "689 Madill\n",
      "690 Dick\n",
      "691 Karun\n",
      "692 Lam\n",
      "693 Saad\n",
      "694 Weir\n",
      "695 Chapman\n",
      "696 Kelly\n",
      "697 Mullens\n",
      "698 Thayer\n",
      "699 Humblen\n",
      "700 Astor\n",
      "701 Silverthorne\n",
      "702 Barbara\n",
      "703 Gallagher\n",
      "704 Hansen\n",
      "705 Morley\n",
      "706 Kelly\n",
      "707 Calderhead\n",
      "708 Cleaver\n",
      "709 Moubarek\n",
      "710 Mayne\n",
      "711 Klaber\n",
      "712 Taylor\n",
      "713 Larsson\n",
      "714 Greenberg\n",
      "715 Soholt\n",
      "716 Endres\n",
      "717 Troutt\n",
      "718 McEvoy\n",
      "719 Johnson\n",
      "720 Harper\n",
      "721 Jensen\n",
      "722 Gillespie\n",
      "723 Hodges\n",
      "724 Chambers\n",
      "725 Oreskovic\n",
      "726 Renouf\n",
      "727 Mannion\n",
      "728 Bryhl\n",
      "729 Ilmakangas\n",
      "730 Allen\n",
      "731 Hassan\n",
      "732 Knight\n",
      "733 Berriman\n",
      "734 Troupiansky\n",
      "735 Williams\n",
      "736 Ford\n",
      "737 Lesurer\n",
      "738 Ivanoff\n",
      "739 Nankoff\n",
      "740 Hawksford\n",
      "741 Cavendish\n",
      "742 Ryerson\n",
      "743 McNamee\n",
      "744 Stranden\n",
      "745 Crosby\n",
      "746 Abbott\n",
      "747 Sinkkonen\n",
      "748 Marvin\n",
      "749 Connaghton\n",
      "750 Wells\n",
      "751 Moor\n",
      "752 Vande Velde\n",
      "753 Jonkoff\n",
      "754 Herman\n",
      "755 Hamalainen\n",
      "756 Carlsson\n",
      "757 Bailey\n",
      "758 Theobald\n",
      "759 Rothes\n",
      "760 Garfirth\n",
      "761 Nirva\n",
      "762 Barah\n",
      "763 Carter\n",
      "764 Eklund\n",
      "765 Hogeboom\n",
      "766 Brewe\n",
      "767 Mangan\n",
      "768 Moran\n",
      "769 Gronnestad\n",
      "770 Lievens\n",
      "771 Jensen\n",
      "772 Mack\n",
      "773 Elias\n",
      "774 Hocking\n",
      "775 Myhrman\n",
      "776 Tobin\n",
      "777 Emanuel\n",
      "778 Kilgannon\n",
      "779 Robert\n",
      "780 Ayoub\n",
      "781 Dick\n",
      "782 Long\n",
      "783 Johnston\n",
      "784 Ali\n",
      "785 Harmer\n",
      "786 Sjoblom\n",
      "787 Rice\n",
      "788 Dean\n",
      "789 Guggenheim\n",
      "790 Keane\n",
      "791 Gaskell\n",
      "792 Sage\n",
      "793 Hoyt\n",
      "794 Dantcheff\n",
      "795 Otter\n",
      "796 Leader\n",
      "797 Osman\n",
      "798 Ibrahim Shawah\n",
      "799 Van Impe\n",
      "800 Ponesell\n",
      "801 Collyer\n",
      "802 Carter\n",
      "803 Thomas\n",
      "804 Hedman\n",
      "805 Johansson\n",
      "806 Andrews\n",
      "807 Pettersson\n",
      "808 Meyer\n",
      "809 Chambers\n",
      "810 Alexander\n",
      "811 Lester\n",
      "812 Slemen\n",
      "813 Andersson\n",
      "814 Tomlin\n",
      "815 Fry\n",
      "816 Heininen\n",
      "817 Mallet\n",
      "818 Holm\n",
      "819 Skoog\n",
      "820 Hays\n",
      "821 Lulic\n",
      "822 Reuchlin\n",
      "823 Moor\n",
      "824 Panula\n",
      "825 Flynn\n",
      "826 Lam\n",
      "827 Mallet\n",
      "828 McCormack\n",
      "829 Stone\n",
      "830 Yasbeck\n",
      "831 Richards\n",
      "832 Saad\n",
      "833 Augustsson\n",
      "834 Allum\n",
      "835 Compton\n",
      "836 Pasic\n",
      "837 Sirota\n",
      "838 Chip\n",
      "839 Marechal\n",
      "840 Alhomaki\n",
      "841 Mudd\n",
      "842 Serepeca\n",
      "843 Lemberopolous\n",
      "844 Culumovic\n",
      "845 Abbing\n",
      "846 Sage\n",
      "847 Markoff\n",
      "848 Harper\n",
      "849 Goldenberg\n",
      "850 Andersson\n",
      "851 Svensson\n",
      "852 Boulos\n",
      "853 Lines\n",
      "854 Carter\n",
      "855 Aks\n",
      "856 Wick\n",
      "857 Daly\n",
      "858 Baclini\n",
      "859 Razi\n",
      "860 Hansen\n",
      "861 Giles\n",
      "862 Swift\n",
      "863 Sage\n",
      "864 Gill\n",
      "865 Bystrom\n",
      "866 Duran y More\n",
      "867 Roebling\n",
      "868 van Melkebeke\n",
      "869 Johnson\n",
      "870 Balkic\n",
      "871 Beckwith\n",
      "872 Carlsson\n",
      "873 Vander Cruyssen\n",
      "874 Abelson\n",
      "875 Najib\n",
      "876 Gustafsson\n",
      "877 Petroff\n",
      "878 Laleff\n",
      "879 Potter\n",
      "880 Shelley\n",
      "881 Markun\n",
      "882 Dahlberg\n",
      "883 Banfield\n",
      "884 Sutehall\n",
      "885 Rice\n",
      "886 Montvila\n",
      "887 Graham\n",
      "888 Johnston\n",
      "889 Behr\n",
      "890 Dooley\n"
     ]
    }
   ],
   "source": [
    "for index, row in df.iterrows():\n",
    "    print(index,row['last'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "93e2ec7d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>last</th>\n",
       "      <th>first</th>\n",
       "      <th>gender</th>\n",
       "      <th>age</th>\n",
       "      <th>class</th>\n",
       "      <th>fare</th>\n",
       "      <th>embarked</th>\n",
       "      <th>survived</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>52</th>\n",
       "      <td>Harper</td>\n",
       "      <td>Mrs. Henry Sleeper (Myna Haxtun)</td>\n",
       "      <td>F</td>\n",
       "      <td>49.0</td>\n",
       "      <td>1</td>\n",
       "      <td>76.7292</td>\n",
       "      <td>Cherbourg</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>645</th>\n",
       "      <td>Harper</td>\n",
       "      <td>Mr. Henry Sleeper</td>\n",
       "      <td>M</td>\n",
       "      <td>48.0</td>\n",
       "      <td>1</td>\n",
       "      <td>76.7292</td>\n",
       "      <td>Cherbourg</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>720</th>\n",
       "      <td>Harper</td>\n",
       "      <td>Miss Annie Jessie \"Nina\"</td>\n",
       "      <td>F</td>\n",
       "      <td>6.0</td>\n",
       "      <td>2</td>\n",
       "      <td>33.0000</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>848</th>\n",
       "      <td>Harper</td>\n",
       "      <td>Rev. John</td>\n",
       "      <td>M</td>\n",
       "      <td>28.0</td>\n",
       "      <td>2</td>\n",
       "      <td>33.0000</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       last                             first gender   age  class     fare  \\\n",
       "52   Harper  Mrs. Henry Sleeper (Myna Haxtun)      F  49.0      1  76.7292   \n",
       "645  Harper                 Mr. Henry Sleeper      M  48.0      1  76.7292   \n",
       "720  Harper          Miss Annie Jessie \"Nina\"      F   6.0      2  33.0000   \n",
       "848  Harper                         Rev. John      M  28.0      2  33.0000   \n",
       "\n",
       "        embarked survived  \n",
       "52     Cherbourg      yes  \n",
       "645    Cherbourg      yes  \n",
       "720  Southampton      yes  \n",
       "848  Southampton       no  "
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[df['last'] == 'Harper']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "f3dfc7c8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>class</th>\n",
       "      <th>fare</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>714.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>29.699118</td>\n",
       "      <td>2.308642</td>\n",
       "      <td>32.204208</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>14.526497</td>\n",
       "      <td>0.836071</td>\n",
       "      <td>49.693429</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.420000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>20.125000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>7.910400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>28.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>14.454200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>38.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>31.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>80.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>512.329200</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              age       class        fare\n",
       "count  714.000000  891.000000  891.000000\n",
       "mean    29.699118    2.308642   32.204208\n",
       "std     14.526497    0.836071   49.693429\n",
       "min      0.420000    1.000000    0.000000\n",
       "25%     20.125000    2.000000    7.910400\n",
       "50%     28.000000    3.000000   14.454200\n",
       "75%     38.000000    3.000000   31.000000\n",
       "max     80.000000    3.000000  512.329200"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "a843c735",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>last</th>\n",
       "      <th>first</th>\n",
       "      <th>gender</th>\n",
       "      <th>age</th>\n",
       "      <th>class</th>\n",
       "      <th>fare</th>\n",
       "      <th>embarked</th>\n",
       "      <th>survived</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>868</th>\n",
       "      <td>van Melkebeke</td>\n",
       "      <td>Mr. Philemon</td>\n",
       "      <td>M</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3</td>\n",
       "      <td>9.5000</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>153</th>\n",
       "      <td>van Billiard</td>\n",
       "      <td>Mr. Austin Blyler</td>\n",
       "      <td>M</td>\n",
       "      <td>40.5</td>\n",
       "      <td>3</td>\n",
       "      <td>14.5000</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>361</th>\n",
       "      <td>del Carlo</td>\n",
       "      <td>Mr. Sebastiano</td>\n",
       "      <td>M</td>\n",
       "      <td>29.0</td>\n",
       "      <td>2</td>\n",
       "      <td>27.7208</td>\n",
       "      <td>Cherbourg</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>282</th>\n",
       "      <td>de Pelsmaeker</td>\n",
       "      <td>Mr. Alfons</td>\n",
       "      <td>M</td>\n",
       "      <td>16.0</td>\n",
       "      <td>3</td>\n",
       "      <td>9.5000</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>286</th>\n",
       "      <td>de Mulder</td>\n",
       "      <td>Mr. Theodore</td>\n",
       "      <td>M</td>\n",
       "      <td>30.0</td>\n",
       "      <td>3</td>\n",
       "      <td>9.5000</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>874</th>\n",
       "      <td>Abelson</td>\n",
       "      <td>Mrs. Samuel (Hannah Wizosky)</td>\n",
       "      <td>F</td>\n",
       "      <td>28.0</td>\n",
       "      <td>2</td>\n",
       "      <td>24.0000</td>\n",
       "      <td>Cherbourg</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>308</th>\n",
       "      <td>Abelson</td>\n",
       "      <td>Mr. Samuel</td>\n",
       "      <td>M</td>\n",
       "      <td>30.0</td>\n",
       "      <td>2</td>\n",
       "      <td>24.0000</td>\n",
       "      <td>Cherbourg</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>746</th>\n",
       "      <td>Abbott</td>\n",
       "      <td>Mr. Rossmore Edward</td>\n",
       "      <td>M</td>\n",
       "      <td>16.0</td>\n",
       "      <td>3</td>\n",
       "      <td>20.2500</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>279</th>\n",
       "      <td>Abbott</td>\n",
       "      <td>Mrs. Stanton (Rosa Hunt)</td>\n",
       "      <td>F</td>\n",
       "      <td>35.0</td>\n",
       "      <td>3</td>\n",
       "      <td>20.2500</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>845</th>\n",
       "      <td>Abbing</td>\n",
       "      <td>Mr. Anthony</td>\n",
       "      <td>M</td>\n",
       "      <td>42.0</td>\n",
       "      <td>3</td>\n",
       "      <td>7.5500</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>891 rows × 8 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "              last                         first gender   age  class     fare  \\\n",
       "868  van Melkebeke                  Mr. Philemon      M   NaN      3   9.5000   \n",
       "153   van Billiard             Mr. Austin Blyler      M  40.5      3  14.5000   \n",
       "361      del Carlo                Mr. Sebastiano      M  29.0      2  27.7208   \n",
       "282  de Pelsmaeker                    Mr. Alfons      M  16.0      3   9.5000   \n",
       "286      de Mulder                  Mr. Theodore      M  30.0      3   9.5000   \n",
       "..             ...                           ...    ...   ...    ...      ...   \n",
       "874        Abelson  Mrs. Samuel (Hannah Wizosky)      F  28.0      2  24.0000   \n",
       "308        Abelson                    Mr. Samuel      M  30.0      2  24.0000   \n",
       "746         Abbott           Mr. Rossmore Edward      M  16.0      3  20.2500   \n",
       "279         Abbott      Mrs. Stanton (Rosa Hunt)      F  35.0      3  20.2500   \n",
       "845         Abbing                   Mr. Anthony      M  42.0      3   7.5500   \n",
       "\n",
       "        embarked survived  \n",
       "868  Southampton       no  \n",
       "153  Southampton       no  \n",
       "361    Cherbourg       no  \n",
       "282  Southampton       no  \n",
       "286  Southampton      yes  \n",
       "..           ...      ...  \n",
       "874    Cherbourg      yes  \n",
       "308    Cherbourg       no  \n",
       "746  Southampton       no  \n",
       "279  Southampton      yes  \n",
       "845  Southampton       no  \n",
       "\n",
       "[891 rows x 8 columns]"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.sort_values('last', ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "a829e985",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>last</th>\n",
       "      <th>first</th>\n",
       "      <th>gender</th>\n",
       "      <th>age</th>\n",
       "      <th>class</th>\n",
       "      <th>fare</th>\n",
       "      <th>embarked</th>\n",
       "      <th>survived</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>868</th>\n",
       "      <td>van Melkebeke</td>\n",
       "      <td>Mr. Philemon</td>\n",
       "      <td>M</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3</td>\n",
       "      <td>9.5000</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>153</th>\n",
       "      <td>van Billiard</td>\n",
       "      <td>Mr. Austin Blyler</td>\n",
       "      <td>M</td>\n",
       "      <td>40.5</td>\n",
       "      <td>3</td>\n",
       "      <td>14.5000</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>361</th>\n",
       "      <td>del Carlo</td>\n",
       "      <td>Mr. Sebastiano</td>\n",
       "      <td>M</td>\n",
       "      <td>29.0</td>\n",
       "      <td>2</td>\n",
       "      <td>27.7208</td>\n",
       "      <td>Cherbourg</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>282</th>\n",
       "      <td>de Pelsmaeker</td>\n",
       "      <td>Mr. Alfons</td>\n",
       "      <td>M</td>\n",
       "      <td>16.0</td>\n",
       "      <td>3</td>\n",
       "      <td>9.5000</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>286</th>\n",
       "      <td>de Mulder</td>\n",
       "      <td>Mr. Theodore</td>\n",
       "      <td>M</td>\n",
       "      <td>30.0</td>\n",
       "      <td>3</td>\n",
       "      <td>9.5000</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>308</th>\n",
       "      <td>Abelson</td>\n",
       "      <td>Mr. Samuel</td>\n",
       "      <td>M</td>\n",
       "      <td>30.0</td>\n",
       "      <td>2</td>\n",
       "      <td>24.0000</td>\n",
       "      <td>Cherbourg</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>874</th>\n",
       "      <td>Abelson</td>\n",
       "      <td>Mrs. Samuel (Hannah Wizosky)</td>\n",
       "      <td>F</td>\n",
       "      <td>28.0</td>\n",
       "      <td>2</td>\n",
       "      <td>24.0000</td>\n",
       "      <td>Cherbourg</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>746</th>\n",
       "      <td>Abbott</td>\n",
       "      <td>Mr. Rossmore Edward</td>\n",
       "      <td>M</td>\n",
       "      <td>16.0</td>\n",
       "      <td>3</td>\n",
       "      <td>20.2500</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>279</th>\n",
       "      <td>Abbott</td>\n",
       "      <td>Mrs. Stanton (Rosa Hunt)</td>\n",
       "      <td>F</td>\n",
       "      <td>35.0</td>\n",
       "      <td>3</td>\n",
       "      <td>20.2500</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>845</th>\n",
       "      <td>Abbing</td>\n",
       "      <td>Mr. Anthony</td>\n",
       "      <td>M</td>\n",
       "      <td>42.0</td>\n",
       "      <td>3</td>\n",
       "      <td>7.5500</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>891 rows × 8 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "              last                         first gender   age  class     fare  \\\n",
       "868  van Melkebeke                  Mr. Philemon      M   NaN      3   9.5000   \n",
       "153   van Billiard             Mr. Austin Blyler      M  40.5      3  14.5000   \n",
       "361      del Carlo                Mr. Sebastiano      M  29.0      2  27.7208   \n",
       "282  de Pelsmaeker                    Mr. Alfons      M  16.0      3   9.5000   \n",
       "286      de Mulder                  Mr. Theodore      M  30.0      3   9.5000   \n",
       "..             ...                           ...    ...   ...    ...      ...   \n",
       "308        Abelson                    Mr. Samuel      M  30.0      2  24.0000   \n",
       "874        Abelson  Mrs. Samuel (Hannah Wizosky)      F  28.0      2  24.0000   \n",
       "746         Abbott           Mr. Rossmore Edward      M  16.0      3  20.2500   \n",
       "279         Abbott      Mrs. Stanton (Rosa Hunt)      F  35.0      3  20.2500   \n",
       "845         Abbing                   Mr. Anthony      M  42.0      3   7.5500   \n",
       "\n",
       "        embarked survived  \n",
       "868  Southampton       no  \n",
       "153  Southampton       no  \n",
       "361    Cherbourg       no  \n",
       "282  Southampton       no  \n",
       "286  Southampton      yes  \n",
       "..           ...      ...  \n",
       "308    Cherbourg       no  \n",
       "874    Cherbourg      yes  \n",
       "746  Southampton       no  \n",
       "279  Southampton      yes  \n",
       "845  Southampton       no  \n",
       "\n",
       "[891 rows x 8 columns]"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.sort_values(['last','first'], ascending=[False,True])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "b93a37ce",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>last</th>\n",
       "      <th>first</th>\n",
       "      <th>gender</th>\n",
       "      <th>age</th>\n",
       "      <th>class</th>\n",
       "      <th>fare</th>\n",
       "      <th>embarked</th>\n",
       "      <th>survived</th>\n",
       "      <th>full name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Braund</td>\n",
       "      <td>Mr. Owen Harris</td>\n",
       "      <td>M</td>\n",
       "      <td>22.0</td>\n",
       "      <td>3</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>Mr. Owen Harris Braund</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Cumings</td>\n",
       "      <td>Mrs. John Bradley (Florence Briggs Thayer)</td>\n",
       "      <td>F</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>Cherbourg</td>\n",
       "      <td>yes</td>\n",
       "      <td>Mrs. John Bradley (Florence Briggs Thayer) Cum...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Heikkinen</td>\n",
       "      <td>Miss Laina</td>\n",
       "      <td>F</td>\n",
       "      <td>26.0</td>\n",
       "      <td>3</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "      <td>Miss Laina Heikkinen</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Futrelle</td>\n",
       "      <td>Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>F</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "      <td>Mrs. Jacques Heath (Lily May Peel) Futrelle</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Allen</td>\n",
       "      <td>Mr. William Henry</td>\n",
       "      <td>M</td>\n",
       "      <td>35.0</td>\n",
       "      <td>3</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>Mr. William Henry Allen</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        last                                       first gender   age  class  \\\n",
       "0     Braund                             Mr. Owen Harris      M  22.0      3   \n",
       "1    Cumings  Mrs. John Bradley (Florence Briggs Thayer)      F  38.0      1   \n",
       "2  Heikkinen                                  Miss Laina      F  26.0      3   \n",
       "3   Futrelle          Mrs. Jacques Heath (Lily May Peel)      F  35.0      1   \n",
       "4      Allen                           Mr. William Henry      M  35.0      3   \n",
       "\n",
       "      fare     embarked survived  \\\n",
       "0   7.2500  Southampton       no   \n",
       "1  71.2833    Cherbourg      yes   \n",
       "2   7.9250  Southampton      yes   \n",
       "3  53.1000  Southampton      yes   \n",
       "4   8.0500  Southampton       no   \n",
       "\n",
       "                                           full name  \n",
       "0                             Mr. Owen Harris Braund  \n",
       "1  Mrs. John Bradley (Florence Briggs Thayer) Cum...  \n",
       "2                               Miss Laina Heikkinen  \n",
       "3        Mrs. Jacques Heath (Lily May Peel) Futrelle  \n",
       "4                            Mr. William Henry Allen  "
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"full name\"] = df[\"first\"]+ \" \" +df[\"last\"]\n",
    "df.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "6c3c3667",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>last</th>\n",
       "      <th>first</th>\n",
       "      <th>gender</th>\n",
       "      <th>age</th>\n",
       "      <th>class</th>\n",
       "      <th>embarked</th>\n",
       "      <th>survived</th>\n",
       "      <th>full name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Braund</td>\n",
       "      <td>Mr. Owen Harris</td>\n",
       "      <td>M</td>\n",
       "      <td>22.0</td>\n",
       "      <td>3</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>Mr. Owen Harris Braund</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Cumings</td>\n",
       "      <td>Mrs. John Bradley (Florence Briggs Thayer)</td>\n",
       "      <td>F</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>Cherbourg</td>\n",
       "      <td>yes</td>\n",
       "      <td>Mrs. John Bradley (Florence Briggs Thayer) Cum...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Heikkinen</td>\n",
       "      <td>Miss Laina</td>\n",
       "      <td>F</td>\n",
       "      <td>26.0</td>\n",
       "      <td>3</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "      <td>Miss Laina Heikkinen</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        last                                       first gender   age  class  \\\n",
       "0     Braund                             Mr. Owen Harris      M  22.0      3   \n",
       "1    Cumings  Mrs. John Bradley (Florence Briggs Thayer)      F  38.0      1   \n",
       "2  Heikkinen                                  Miss Laina      F  26.0      3   \n",
       "\n",
       "      embarked survived                                          full name  \n",
       "0  Southampton       no                             Mr. Owen Harris Braund  \n",
       "1    Cherbourg      yes  Mrs. John Bradley (Florence Briggs Thayer) Cum...  \n",
       "2  Southampton      yes                               Miss Laina Heikkinen  "
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "newdf = df.drop(columns =[\"fare\"] )\n",
    "newdf.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "ed0286e6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>fare</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>7.2500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>71.2833</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>7.9250</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>53.1000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>8.0500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>886</th>\n",
       "      <td>13.0000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>887</th>\n",
       "      <td>30.0000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>23.4500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>30.0000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>7.7500</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>891 rows × 1 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        fare\n",
       "0     7.2500\n",
       "1    71.2833\n",
       "2     7.9250\n",
       "3    53.1000\n",
       "4     8.0500\n",
       "..       ...\n",
       "886  13.0000\n",
       "887  30.0000\n",
       "888  23.4500\n",
       "889  30.0000\n",
       "890   7.7500\n",
       "\n",
       "[891 rows x 1 columns]"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.iloc[:,5:6]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "aff44477",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>last</th>\n",
       "      <th>first</th>\n",
       "      <th>gender</th>\n",
       "      <th>age</th>\n",
       "      <th>class</th>\n",
       "      <th>fare</th>\n",
       "      <th>embarked</th>\n",
       "      <th>survived</th>\n",
       "      <th>full name</th>\n",
       "      <th>total</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Braund</td>\n",
       "      <td>Mr. Owen Harris</td>\n",
       "      <td>M</td>\n",
       "      <td>22.0</td>\n",
       "      <td>3</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>Mr. Owen Harris Braund</td>\n",
       "      <td>7.2500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Cumings</td>\n",
       "      <td>Mrs. John Bradley (Florence Briggs Thayer)</td>\n",
       "      <td>F</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>Cherbourg</td>\n",
       "      <td>yes</td>\n",
       "      <td>Mrs. John Bradley (Florence Briggs Thayer) Cum...</td>\n",
       "      <td>71.2833</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Heikkinen</td>\n",
       "      <td>Miss Laina</td>\n",
       "      <td>F</td>\n",
       "      <td>26.0</td>\n",
       "      <td>3</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "      <td>Miss Laina Heikkinen</td>\n",
       "      <td>7.9250</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        last                                       first gender   age  class  \\\n",
       "0     Braund                             Mr. Owen Harris      M  22.0      3   \n",
       "1    Cumings  Mrs. John Bradley (Florence Briggs Thayer)      F  38.0      1   \n",
       "2  Heikkinen                                  Miss Laina      F  26.0      3   \n",
       "\n",
       "      fare     embarked survived  \\\n",
       "0   7.2500  Southampton       no   \n",
       "1  71.2833    Cherbourg      yes   \n",
       "2   7.9250  Southampton      yes   \n",
       "\n",
       "                                           full name    total  \n",
       "0                             Mr. Owen Harris Braund   7.2500  \n",
       "1  Mrs. John Bradley (Florence Briggs Thayer) Cum...  71.2833  \n",
       "2                               Miss Laina Heikkinen   7.9250  "
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['total'] = df.iloc[:,5:6].sum(axis=1)\n",
    "df.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "a966390a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['last',\n",
       " 'first',\n",
       " 'gender',\n",
       " 'age',\n",
       " 'class',\n",
       " 'fare',\n",
       " 'embarked',\n",
       " 'survived',\n",
       " 'full name',\n",
       " 'total']"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cols = list(df.columns.values)\n",
    "cols"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "edf40d13",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>last</th>\n",
       "      <th>first</th>\n",
       "      <th>gender</th>\n",
       "      <th>age</th>\n",
       "      <th>class</th>\n",
       "      <th>fare</th>\n",
       "      <th>embarked</th>\n",
       "      <th>survived</th>\n",
       "      <th>full name</th>\n",
       "      <th>total</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Braund</td>\n",
       "      <td>Mr. Owen Harris</td>\n",
       "      <td>M</td>\n",
       "      <td>22.0</td>\n",
       "      <td>3</td>\n",
       "      <td>7.25</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>Mr. Owen Harris Braund</td>\n",
       "      <td>7.25</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     last            first gender   age  class  fare     embarked survived  \\\n",
       "0  Braund  Mr. Owen Harris      M  22.0      3  7.25  Southampton       no   \n",
       "\n",
       "                full name  total  \n",
       "0  Mr. Owen Harris Braund   7.25  "
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# df1 = df.loc[(df['first'] == \"Mr. Owen Harris\") & (df['last'] == \"Braund\")]\n",
    "df.loc[df['first'] == \"Mr. Owen Harris\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "f17a44d8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>last</th>\n",
       "      <th>first</th>\n",
       "      <th>gender</th>\n",
       "      <th>age</th>\n",
       "      <th>class</th>\n",
       "      <th>fare</th>\n",
       "      <th>embarked</th>\n",
       "      <th>survived</th>\n",
       "      <th>full name</th>\n",
       "      <th>total</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Heikkinen</td>\n",
       "      <td>Miss Laina</td>\n",
       "      <td>F</td>\n",
       "      <td>26.0</td>\n",
       "      <td>3</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "      <td>Miss Laina Heikkinen</td>\n",
       "      <td>7.9250</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Palsson</td>\n",
       "      <td>Master Gosta Leonard</td>\n",
       "      <td>M</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3</td>\n",
       "      <td>21.0750</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>Master Gosta Leonard Palsson</td>\n",
       "      <td>21.0750</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Sandstrom</td>\n",
       "      <td>Miss Marguerite Rut</td>\n",
       "      <td>F</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3</td>\n",
       "      <td>16.7000</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "      <td>Miss Marguerite Rut Sandstrom</td>\n",
       "      <td>16.7000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Bonnell</td>\n",
       "      <td>Miss Elizabeth</td>\n",
       "      <td>F</td>\n",
       "      <td>58.0</td>\n",
       "      <td>1</td>\n",
       "      <td>26.5500</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "      <td>Miss Elizabeth Bonnell</td>\n",
       "      <td>26.5500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>Vestrom</td>\n",
       "      <td>Miss Hulda Amanda Adolfina</td>\n",
       "      <td>F</td>\n",
       "      <td>14.0</td>\n",
       "      <td>3</td>\n",
       "      <td>7.8542</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>Miss Hulda Amanda Adolfina Vestrom</td>\n",
       "      <td>7.8542</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>875</th>\n",
       "      <td>Najib</td>\n",
       "      <td>Miss Adele Kiamie \"Jane\"</td>\n",
       "      <td>F</td>\n",
       "      <td>15.0</td>\n",
       "      <td>3</td>\n",
       "      <td>7.2250</td>\n",
       "      <td>Cherbourg</td>\n",
       "      <td>yes</td>\n",
       "      <td>Miss Adele Kiamie \"Jane\" Najib</td>\n",
       "      <td>7.2250</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>882</th>\n",
       "      <td>Dahlberg</td>\n",
       "      <td>Miss Gerda Ulrika</td>\n",
       "      <td>F</td>\n",
       "      <td>22.0</td>\n",
       "      <td>3</td>\n",
       "      <td>10.5167</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>Miss Gerda Ulrika Dahlberg</td>\n",
       "      <td>10.5167</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>886</th>\n",
       "      <td>Montvila</td>\n",
       "      <td>Rev. Juozas</td>\n",
       "      <td>M</td>\n",
       "      <td>27.0</td>\n",
       "      <td>2</td>\n",
       "      <td>13.0000</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>Rev. Juozas Montvila</td>\n",
       "      <td>13.0000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>887</th>\n",
       "      <td>Graham</td>\n",
       "      <td>Miss Margaret Edith</td>\n",
       "      <td>F</td>\n",
       "      <td>19.0</td>\n",
       "      <td>1</td>\n",
       "      <td>30.0000</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "      <td>Miss Margaret Edith Graham</td>\n",
       "      <td>30.0000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>Johnston</td>\n",
       "      <td>Miss Catherine Helen \"Carrie\"</td>\n",
       "      <td>F</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3</td>\n",
       "      <td>23.4500</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>Miss Catherine Helen \"Carrie\" Johnston</td>\n",
       "      <td>23.4500</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>244 rows × 10 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "          last                           first gender   age  class     fare  \\\n",
       "2    Heikkinen                      Miss Laina      F  26.0      3   7.9250   \n",
       "7      Palsson            Master Gosta Leonard      M   2.0      3  21.0750   \n",
       "10   Sandstrom             Miss Marguerite Rut      F   4.0      3  16.7000   \n",
       "11     Bonnell                  Miss Elizabeth      F  58.0      1  26.5500   \n",
       "14     Vestrom      Miss Hulda Amanda Adolfina      F  14.0      3   7.8542   \n",
       "..         ...                             ...    ...   ...    ...      ...   \n",
       "875      Najib        Miss Adele Kiamie \"Jane\"      F  15.0      3   7.2250   \n",
       "882   Dahlberg               Miss Gerda Ulrika      F  22.0      3  10.5167   \n",
       "886   Montvila                     Rev. Juozas      M  27.0      2  13.0000   \n",
       "887     Graham             Miss Margaret Edith      F  19.0      1  30.0000   \n",
       "888   Johnston   Miss Catherine Helen \"Carrie\"      F   NaN      3  23.4500   \n",
       "\n",
       "        embarked survived                                full name    total  \n",
       "2    Southampton      yes                     Miss Laina Heikkinen   7.9250  \n",
       "7    Southampton       no             Master Gosta Leonard Palsson  21.0750  \n",
       "10   Southampton      yes            Miss Marguerite Rut Sandstrom  16.7000  \n",
       "11   Southampton      yes                   Miss Elizabeth Bonnell  26.5500  \n",
       "14   Southampton       no       Miss Hulda Amanda Adolfina Vestrom   7.8542  \n",
       "..           ...      ...                                      ...      ...  \n",
       "875    Cherbourg      yes           Miss Adele Kiamie \"Jane\" Najib   7.2250  \n",
       "882  Southampton       no               Miss Gerda Ulrika Dahlberg  10.5167  \n",
       "886  Southampton       no                     Rev. Juozas Montvila  13.0000  \n",
       "887  Southampton      yes               Miss Margaret Edith Graham  30.0000  \n",
       "888  Southampton       no   Miss Catherine Helen \"Carrie\" Johnston  23.4500  \n",
       "\n",
       "[244 rows x 10 columns]"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1 = df.loc[~df['first'].str.contains('Mr')]\n",
    "df1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "b9626460",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>last</th>\n",
       "      <th>first</th>\n",
       "      <th>gender</th>\n",
       "      <th>age</th>\n",
       "      <th>class</th>\n",
       "      <th>fare</th>\n",
       "      <th>embarked</th>\n",
       "      <th>survived</th>\n",
       "      <th>full name</th>\n",
       "      <th>total</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>51</th>\n",
       "      <td>Nosworthy</td>\n",
       "      <td>Mr. Richard Cater</td>\n",
       "      <td>M</td>\n",
       "      <td>21.0</td>\n",
       "      <td>3</td>\n",
       "      <td>7.8000</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>Mr. Richard Cater Nosworthy</td>\n",
       "      <td>7.8000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>85</th>\n",
       "      <td>Backstrom</td>\n",
       "      <td>Mrs. Karl Alfred (Maria Mathilda Gustafsson)</td>\n",
       "      <td>F</td>\n",
       "      <td>33.0</td>\n",
       "      <td>3</td>\n",
       "      <td>15.8500</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "      <td>Mrs. Karl Alfred (Maria Mathilda Gustafsson) B...</td>\n",
       "      <td>15.8500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>100</th>\n",
       "      <td>Petranec</td>\n",
       "      <td>Miss Matilda</td>\n",
       "      <td>F</td>\n",
       "      <td>28.0</td>\n",
       "      <td>3</td>\n",
       "      <td>7.8958</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>Miss Matilda Petranec</td>\n",
       "      <td>7.8958</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>133</th>\n",
       "      <td>Weisz</td>\n",
       "      <td>Mrs. Leopold (Mathilde Francoise Pede)</td>\n",
       "      <td>F</td>\n",
       "      <td>29.0</td>\n",
       "      <td>2</td>\n",
       "      <td>26.0000</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "      <td>Mrs. Leopold (Mathilde Francoise Pede) Weisz</td>\n",
       "      <td>26.0000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>142</th>\n",
       "      <td>Hakkarainen</td>\n",
       "      <td>Mrs. Pekka Pietari (Elin Matilda Dolck)</td>\n",
       "      <td>F</td>\n",
       "      <td>24.0</td>\n",
       "      <td>3</td>\n",
       "      <td>15.8500</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "      <td>Mrs. Pekka Pietari (Elin Matilda Dolck) Hakkar...</td>\n",
       "      <td>15.8500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>205</th>\n",
       "      <td>Strom</td>\n",
       "      <td>Miss Telma Matilda</td>\n",
       "      <td>F</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3</td>\n",
       "      <td>10.4625</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>Miss Telma Matilda Strom</td>\n",
       "      <td>10.4625</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>229</th>\n",
       "      <td>Lefebre</td>\n",
       "      <td>Miss Mathilde</td>\n",
       "      <td>F</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3</td>\n",
       "      <td>25.4667</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>Miss Mathilde Lefebre</td>\n",
       "      <td>25.4667</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>243</th>\n",
       "      <td>Maenpaa</td>\n",
       "      <td>Mr. Matti Alexanteri</td>\n",
       "      <td>M</td>\n",
       "      <td>22.0</td>\n",
       "      <td>3</td>\n",
       "      <td>7.1250</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>Mr. Matti Alexanteri Maenpaa</td>\n",
       "      <td>7.1250</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>251</th>\n",
       "      <td>Strom</td>\n",
       "      <td>Mrs. Wilhelm (Elna Matilda Persson)</td>\n",
       "      <td>F</td>\n",
       "      <td>29.0</td>\n",
       "      <td>3</td>\n",
       "      <td>10.4625</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>Mrs. Wilhelm (Elna Matilda Persson) Strom</td>\n",
       "      <td>10.4625</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>362</th>\n",
       "      <td>Barbara</td>\n",
       "      <td>Mrs. (Catherine David)</td>\n",
       "      <td>F</td>\n",
       "      <td>45.0</td>\n",
       "      <td>3</td>\n",
       "      <td>14.4542</td>\n",
       "      <td>Cherbourg</td>\n",
       "      <td>no</td>\n",
       "      <td>Mrs. (Catherine David) Barbara</td>\n",
       "      <td>14.4542</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>388</th>\n",
       "      <td>Sadlier</td>\n",
       "      <td>Mr. Matthew</td>\n",
       "      <td>M</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3</td>\n",
       "      <td>7.7292</td>\n",
       "      <td>Queenstown</td>\n",
       "      <td>no</td>\n",
       "      <td>Mr. Matthew Sadlier</td>\n",
       "      <td>7.7292</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>419</th>\n",
       "      <td>Van Impe</td>\n",
       "      <td>Miss Catharina</td>\n",
       "      <td>F</td>\n",
       "      <td>10.0</td>\n",
       "      <td>3</td>\n",
       "      <td>24.1500</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>Miss Catharina Van Impe</td>\n",
       "      <td>24.1500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>448</th>\n",
       "      <td>Baclini</td>\n",
       "      <td>Miss Marie Catherine</td>\n",
       "      <td>F</td>\n",
       "      <td>5.0</td>\n",
       "      <td>3</td>\n",
       "      <td>19.2583</td>\n",
       "      <td>Cherbourg</td>\n",
       "      <td>yes</td>\n",
       "      <td>Miss Marie Catherine Baclini</td>\n",
       "      <td>19.2583</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>490</th>\n",
       "      <td>Hagland</td>\n",
       "      <td>Mr. Konrad Mathias Reiersen</td>\n",
       "      <td>M</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3</td>\n",
       "      <td>19.9667</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>Mr. Konrad Mathias Reiersen Hagland</td>\n",
       "      <td>19.9667</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>533</th>\n",
       "      <td>Peter</td>\n",
       "      <td>Mrs. Catherine (Catherine Rizk)</td>\n",
       "      <td>F</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3</td>\n",
       "      <td>22.3583</td>\n",
       "      <td>Cherbourg</td>\n",
       "      <td>yes</td>\n",
       "      <td>Mrs. Catherine (Catherine Rizk) Peter</td>\n",
       "      <td>22.3583</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>590</th>\n",
       "      <td>Rintamaki</td>\n",
       "      <td>Mr. Matti</td>\n",
       "      <td>M</td>\n",
       "      <td>35.0</td>\n",
       "      <td>3</td>\n",
       "      <td>7.1250</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>Mr. Matti Rintamaki</td>\n",
       "      <td>7.1250</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>657</th>\n",
       "      <td>Bourke</td>\n",
       "      <td>Mrs. John (Catherine)</td>\n",
       "      <td>F</td>\n",
       "      <td>32.0</td>\n",
       "      <td>3</td>\n",
       "      <td>15.5000</td>\n",
       "      <td>Queenstown</td>\n",
       "      <td>no</td>\n",
       "      <td>Mrs. John (Catherine) Bourke</td>\n",
       "      <td>15.5000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>670</th>\n",
       "      <td>Brown</td>\n",
       "      <td>Mrs. Thomas William Solomon (Elizabeth Catheri...</td>\n",
       "      <td>F</td>\n",
       "      <td>40.0</td>\n",
       "      <td>2</td>\n",
       "      <td>39.0000</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "      <td>Mrs. Thomas William Solomon (Elizabeth Catheri...</td>\n",
       "      <td>39.0000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>699</th>\n",
       "      <td>Humblen</td>\n",
       "      <td>Mr. Adolf Mathias Nicolai Olsen</td>\n",
       "      <td>M</td>\n",
       "      <td>42.0</td>\n",
       "      <td>3</td>\n",
       "      <td>7.6500</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>Mr. Adolf Mathias Nicolai Olsen Humblen</td>\n",
       "      <td>7.6500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>Johnston</td>\n",
       "      <td>Miss Catherine Helen \"Carrie\"</td>\n",
       "      <td>F</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3</td>\n",
       "      <td>23.4500</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>Miss Catherine Helen \"Carrie\" Johnston</td>\n",
       "      <td>23.4500</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            last                                              first gender  \\\n",
       "51     Nosworthy                                  Mr. Richard Cater      M   \n",
       "85     Backstrom       Mrs. Karl Alfred (Maria Mathilda Gustafsson)      F   \n",
       "100     Petranec                                       Miss Matilda      F   \n",
       "133        Weisz             Mrs. Leopold (Mathilde Francoise Pede)      F   \n",
       "142  Hakkarainen            Mrs. Pekka Pietari (Elin Matilda Dolck)      F   \n",
       "205        Strom                                 Miss Telma Matilda      F   \n",
       "229      Lefebre                                      Miss Mathilde      F   \n",
       "243      Maenpaa                               Mr. Matti Alexanteri      M   \n",
       "251        Strom                Mrs. Wilhelm (Elna Matilda Persson)      F   \n",
       "362      Barbara                             Mrs. (Catherine David)      F   \n",
       "388      Sadlier                                        Mr. Matthew      M   \n",
       "419     Van Impe                                     Miss Catharina      F   \n",
       "448      Baclini                               Miss Marie Catherine      F   \n",
       "490      Hagland                        Mr. Konrad Mathias Reiersen      M   \n",
       "533        Peter                    Mrs. Catherine (Catherine Rizk)      F   \n",
       "590    Rintamaki                                          Mr. Matti      M   \n",
       "657       Bourke                              Mrs. John (Catherine)      F   \n",
       "670        Brown  Mrs. Thomas William Solomon (Elizabeth Catheri...      F   \n",
       "699      Humblen                    Mr. Adolf Mathias Nicolai Olsen      M   \n",
       "888     Johnston                      Miss Catherine Helen \"Carrie\"      F   \n",
       "\n",
       "      age  class     fare     embarked survived  \\\n",
       "51   21.0      3   7.8000  Southampton       no   \n",
       "85   33.0      3  15.8500  Southampton      yes   \n",
       "100  28.0      3   7.8958  Southampton       no   \n",
       "133  29.0      2  26.0000  Southampton      yes   \n",
       "142  24.0      3  15.8500  Southampton      yes   \n",
       "205   2.0      3  10.4625  Southampton       no   \n",
       "229   NaN      3  25.4667  Southampton       no   \n",
       "243  22.0      3   7.1250  Southampton       no   \n",
       "251  29.0      3  10.4625  Southampton       no   \n",
       "362  45.0      3  14.4542    Cherbourg       no   \n",
       "388   NaN      3   7.7292   Queenstown       no   \n",
       "419  10.0      3  24.1500  Southampton       no   \n",
       "448   5.0      3  19.2583    Cherbourg      yes   \n",
       "490   NaN      3  19.9667  Southampton       no   \n",
       "533   NaN      3  22.3583    Cherbourg      yes   \n",
       "590  35.0      3   7.1250  Southampton       no   \n",
       "657  32.0      3  15.5000   Queenstown       no   \n",
       "670  40.0      2  39.0000  Southampton      yes   \n",
       "699  42.0      3   7.6500  Southampton       no   \n",
       "888   NaN      3  23.4500  Southampton       no   \n",
       "\n",
       "                                             full name    total  \n",
       "51                         Mr. Richard Cater Nosworthy   7.8000  \n",
       "85   Mrs. Karl Alfred (Maria Mathilda Gustafsson) B...  15.8500  \n",
       "100                              Miss Matilda Petranec   7.8958  \n",
       "133       Mrs. Leopold (Mathilde Francoise Pede) Weisz  26.0000  \n",
       "142  Mrs. Pekka Pietari (Elin Matilda Dolck) Hakkar...  15.8500  \n",
       "205                           Miss Telma Matilda Strom  10.4625  \n",
       "229                              Miss Mathilde Lefebre  25.4667  \n",
       "243                       Mr. Matti Alexanteri Maenpaa   7.1250  \n",
       "251          Mrs. Wilhelm (Elna Matilda Persson) Strom  10.4625  \n",
       "362                     Mrs. (Catherine David) Barbara  14.4542  \n",
       "388                                Mr. Matthew Sadlier   7.7292  \n",
       "419                            Miss Catharina Van Impe  24.1500  \n",
       "448                       Miss Marie Catherine Baclini  19.2583  \n",
       "490                Mr. Konrad Mathias Reiersen Hagland  19.9667  \n",
       "533              Mrs. Catherine (Catherine Rizk) Peter  22.3583  \n",
       "590                                Mr. Matti Rintamaki   7.1250  \n",
       "657                       Mrs. John (Catherine) Bourke  15.5000  \n",
       "670  Mrs. Thomas William Solomon (Elizabeth Catheri...  39.0000  \n",
       "699            Mr. Adolf Mathias Nicolai Olsen Humblen   7.6500  \n",
       "888             Miss Catherine Helen \"Carrie\" Johnston  23.4500  "
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import re\n",
    "\n",
    "df1 = df.loc[df['first'].str.contains('Cat|Mat', regex = True)]\n",
    "df1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "6b4fc619",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>last</th>\n",
       "      <th>first</th>\n",
       "      <th>gender</th>\n",
       "      <th>age</th>\n",
       "      <th>class</th>\n",
       "      <th>fare</th>\n",
       "      <th>embarked</th>\n",
       "      <th>survived</th>\n",
       "      <th>full name</th>\n",
       "      <th>total</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Braund</td>\n",
       "      <td>Mr. Owen Harris</td>\n",
       "      <td>M</td>\n",
       "      <td>22.0</td>\n",
       "      <td>3</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>Mr. Owen Harris Braund</td>\n",
       "      <td>7.2500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Cumings</td>\n",
       "      <td>Mrs. John Bradley (Florence Briggs Thayer)</td>\n",
       "      <td>F</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>Cherbourg</td>\n",
       "      <td>yes</td>\n",
       "      <td>Mrs. John Bradley (Florence Briggs Thayer) Cum...</td>\n",
       "      <td>71.2833</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Heikkinen</td>\n",
       "      <td>Miss Laina</td>\n",
       "      <td>F</td>\n",
       "      <td>26.0</td>\n",
       "      <td>3</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "      <td>Miss Laina Heikkinen</td>\n",
       "      <td>7.9250</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Futrelle</td>\n",
       "      <td>Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>F</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "      <td>Mrs. Jacques Heath (Lily May Peel) Futrelle</td>\n",
       "      <td>53.1000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Allen</td>\n",
       "      <td>Mr. William Henry</td>\n",
       "      <td>M</td>\n",
       "      <td>35.0</td>\n",
       "      <td>3</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>Mr. William Henry Allen</td>\n",
       "      <td>8.0500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>886</th>\n",
       "      <td>Montvila</td>\n",
       "      <td>Rev. Juozas</td>\n",
       "      <td>M</td>\n",
       "      <td>27.0</td>\n",
       "      <td>2</td>\n",
       "      <td>13.0000</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>Rev. Juozas Montvila</td>\n",
       "      <td>13.0000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>887</th>\n",
       "      <td>Graham</td>\n",
       "      <td>Miss Margaret Edith</td>\n",
       "      <td>F</td>\n",
       "      <td>19.0</td>\n",
       "      <td>1</td>\n",
       "      <td>30.0000</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>yes</td>\n",
       "      <td>Miss Margaret Edith Graham</td>\n",
       "      <td>30.0000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>Johnston</td>\n",
       "      <td>Miss Catherine Helen \"Carrie\"</td>\n",
       "      <td>F</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3</td>\n",
       "      <td>23.4500</td>\n",
       "      <td>Southampton</td>\n",
       "      <td>no</td>\n",
       "      <td>Miss Catherine Helen \"Carrie\" Johnston</td>\n",
       "      <td>23.4500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>Behr</td>\n",
       "      <td>Mr. Karl Howell</td>\n",
       "      <td>M</td>\n",
       "      <td>26.0</td>\n",
       "      <td>1</td>\n",
       "      <td>30.0000</td>\n",
       "      <td>Cherbourg</td>\n",
       "      <td>yes</td>\n",
       "      <td>Mr. Karl Howell Behr</td>\n",
       "      <td>30.0000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>Dooley</td>\n",
       "      <td>Mr. Patrick</td>\n",
       "      <td>M</td>\n",
       "      <td>32.0</td>\n",
       "      <td>3</td>\n",
       "      <td>7.7500</td>\n",
       "      <td>Queenstown</td>\n",
       "      <td>no</td>\n",
       "      <td>Mr. Patrick Dooley</td>\n",
       "      <td>7.7500</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>891 rows × 10 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "          last                                       first gender   age  \\\n",
       "0       Braund                             Mr. Owen Harris      M  22.0   \n",
       "1      Cumings  Mrs. John Bradley (Florence Briggs Thayer)      F  38.0   \n",
       "2    Heikkinen                                  Miss Laina      F  26.0   \n",
       "3     Futrelle          Mrs. Jacques Heath (Lily May Peel)      F  35.0   \n",
       "4        Allen                           Mr. William Henry      M  35.0   \n",
       "..         ...                                         ...    ...   ...   \n",
       "886   Montvila                                 Rev. Juozas      M  27.0   \n",
       "887     Graham                         Miss Margaret Edith      F  19.0   \n",
       "888   Johnston               Miss Catherine Helen \"Carrie\"      F   NaN   \n",
       "889       Behr                             Mr. Karl Howell      M  26.0   \n",
       "890     Dooley                                 Mr. Patrick      M  32.0   \n",
       "\n",
       "     class     fare     embarked survived  \\\n",
       "0        3   7.2500  Southampton       no   \n",
       "1        1  71.2833    Cherbourg      yes   \n",
       "2        3   7.9250  Southampton      yes   \n",
       "3        1  53.1000  Southampton      yes   \n",
       "4        3   8.0500  Southampton       no   \n",
       "..     ...      ...          ...      ...   \n",
       "886      2  13.0000  Southampton       no   \n",
       "887      1  30.0000  Southampton      yes   \n",
       "888      3  23.4500  Southampton       no   \n",
       "889      1  30.0000    Cherbourg      yes   \n",
       "890      3   7.7500   Queenstown       no   \n",
       "\n",
       "                                             full name    total  \n",
       "0                               Mr. Owen Harris Braund   7.2500  \n",
       "1    Mrs. John Bradley (Florence Briggs Thayer) Cum...  71.2833  \n",
       "2                                 Miss Laina Heikkinen   7.9250  \n",
       "3          Mrs. Jacques Heath (Lily May Peel) Futrelle  53.1000  \n",
       "4                              Mr. William Henry Allen   8.0500  \n",
       "..                                                 ...      ...  \n",
       "886                               Rev. Juozas Montvila  13.0000  \n",
       "887                         Miss Margaret Edith Graham  30.0000  \n",
       "888             Miss Catherine Helen \"Carrie\" Johnston  23.4500  \n",
       "889                               Mr. Karl Howell Behr  30.0000  \n",
       "890                                 Mr. Patrick Dooley   7.7500  \n",
       "\n",
       "[891 rows x 10 columns]"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "75bd62c6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>fare</th>\n",
       "      <th>total</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>class</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>7111.42</td>\n",
       "      <td>18177.4125</td>\n",
       "      <td>18177.4125</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>5168.83</td>\n",
       "      <td>3801.8417</td>\n",
       "      <td>3801.8417</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>8924.92</td>\n",
       "      <td>6714.6951</td>\n",
       "      <td>6714.6951</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           age        fare       total\n",
       "class                                 \n",
       "1      7111.42  18177.4125  18177.4125\n",
       "2      5168.83   3801.8417   3801.8417\n",
       "3      8924.92   6714.6951   6714.6951"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby([\"class\"]).sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "98d04829",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>fare</th>\n",
       "      <th>total</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>class</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>5168.83</td>\n",
       "      <td>3801.8417</td>\n",
       "      <td>3801.8417</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>8924.92</td>\n",
       "      <td>6714.6951</td>\n",
       "      <td>6714.6951</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>7111.42</td>\n",
       "      <td>18177.4125</td>\n",
       "      <td>18177.4125</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           age        fare       total\n",
       "class                                 \n",
       "2      5168.83   3801.8417   3801.8417\n",
       "3      8924.92   6714.6951   6714.6951\n",
       "1      7111.42  18177.4125  18177.4125"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby([\"class\"]).sum().sort_values(['total'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "5fb5915a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>last</th>\n",
       "      <th>first</th>\n",
       "      <th>gender</th>\n",
       "      <th>age</th>\n",
       "      <th>fare</th>\n",
       "      <th>embarked</th>\n",
       "      <th>survived</th>\n",
       "      <th>full name</th>\n",
       "      <th>total</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>class</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>216</td>\n",
       "      <td>216</td>\n",
       "      <td>216</td>\n",
       "      <td>186</td>\n",
       "      <td>216</td>\n",
       "      <td>216</td>\n",
       "      <td>216</td>\n",
       "      <td>216</td>\n",
       "      <td>216</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>184</td>\n",
       "      <td>184</td>\n",
       "      <td>184</td>\n",
       "      <td>173</td>\n",
       "      <td>184</td>\n",
       "      <td>184</td>\n",
       "      <td>184</td>\n",
       "      <td>184</td>\n",
       "      <td>184</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>491</td>\n",
       "      <td>491</td>\n",
       "      <td>491</td>\n",
       "      <td>355</td>\n",
       "      <td>491</td>\n",
       "      <td>491</td>\n",
       "      <td>491</td>\n",
       "      <td>491</td>\n",
       "      <td>491</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       last  first  gender  age  fare  embarked  survived  full name  total\n",
       "class                                                                      \n",
       "1       216    216     216  186   216       216       216        216    216\n",
       "2       184    184     184  173   184       184       184        184    184\n",
       "3       491    491     491  355   491       491       491        491    491"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " df.groupby([\"class\"]).count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ee6b2bfc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
