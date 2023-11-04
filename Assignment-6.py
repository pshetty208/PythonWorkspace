{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "32898ffe",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "271503e6",
   "metadata": {},
   "source": [
    "# Shingles"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "cd5b885b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def shingles(d0,d1,n):\n",
    "    a = []\n",
    "    b = []\n",
    "    for i in range(0,len(d0)):\n",
    "        if(i<=len(d0)-n):\n",
    "            a.append(d0[i:i+n])\n",
    "    a = set(tuple(x) for x in a)\n",
    "    print(a)\n",
    "    \n",
    "    for i in range(0,len(d1)):\n",
    "        if(i<=len(d1)-n):\n",
    "            b.append(d1[i:i+n])\n",
    "    b = set(tuple(x) for x in b)\n",
    "    print(b)\n",
    "    \n",
    "    res = len(a.intersection(b))/len(a.union(b))\n",
    "    \n",
    "    \n",
    "    print(res)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "36af7c52",
   "metadata": {},
   "outputs": [],
   "source": [
    "d0 = (\"data is the new oil of digital economy\").split()\n",
    "d1 = (\"data is the new oil\").split()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "75d87ae1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{('of', 'digital'), ('data', 'is'), ('the', 'new'), ('digital', 'economy'), ('new', 'oil'), ('is', 'the'), ('oil', 'of')}\n",
      "{('new', 'oil'), ('is', 'the'), ('data', 'is'), ('the', 'new')}\n",
      "0.5714285714285714\n"
     ]
    }
   ],
   "source": [
    "shingles(d0,d1,2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f13621fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{('new', 'oil', 'of'), ('is', 'the', 'new'), ('data', 'is', 'the'), ('the', 'new', 'oil'), ('oil', 'of', 'digital'), ('of', 'digital', 'economy')}\n",
      "{('data', 'is', 'the'), ('the', 'new', 'oil'), ('is', 'the', 'new')}\n",
      "0.5\n"
     ]
    }
   ],
   "source": [
    "shingles(d0,d1,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "8b6fa6f4",
   "metadata": {},
   "outputs": [],
   "source": [
    "d2 = (\"there is an art to getting your way and throwing bananas on the street is not it\").split()\n",
    "d3 = (\"it is not often you find soggy bananas on the street\").split()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "18aeeaeb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{('way', 'and'), ('art', 'to'), ('and', 'throwing'), ('your', 'way'), ('street', 'is'), ('an', 'art'), ('not', 'it'), ('throwing', 'bananas'), ('is', 'an'), ('bananas', 'on'), ('the', 'street'), ('on', 'the'), ('is', 'not'), ('to', 'getting'), ('there', 'is'), ('getting', 'your')}\n",
      "{('not', 'often'), ('it', 'is'), ('soggy', 'bananas'), ('bananas', 'on'), ('you', 'find'), ('find', 'soggy'), ('on', 'the'), ('is', 'not'), ('often', 'you'), ('the', 'street')}\n",
      "0.18181818181818182\n"
     ]
    }
   ],
   "source": [
    "shingles(d2,d3,2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "12a2fa8c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{('art', 'to', 'getting'), ('is', 'an', 'art'), ('street', 'is', 'not'), ('and', 'throwing', 'bananas'), ('an', 'art', 'to'), ('on', 'the', 'street'), ('throwing', 'bananas', 'on'), ('the', 'street', 'is'), ('getting', 'your', 'way'), ('your', 'way', 'and'), ('way', 'and', 'throwing'), ('to', 'getting', 'your'), ('bananas', 'on', 'the'), ('there', 'is', 'an'), ('is', 'not', 'it')}\n",
      "{('find', 'soggy', 'bananas'), ('on', 'the', 'street'), ('it', 'is', 'not'), ('not', 'often', 'you'), ('soggy', 'bananas', 'on'), ('you', 'find', 'soggy'), ('often', 'you', 'find'), ('bananas', 'on', 'the'), ('is', 'not', 'often')}\n",
      "0.09090909090909091\n"
     ]
    }
   ],
   "source": [
    "shingles(d2,d3,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f8379b28",
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
