{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b7abf1a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import math"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "282ef0fe",
   "metadata": {},
   "outputs": [],
   "source": [
    "D0 = \"king palace jungle sleeps\"\n",
    "D1 = \"jungle lion fire king discovery\"\n",
    "D2 = \"king timon mufasa\"\n",
    "D3 = \"timon lion simba\"\n",
    "q = \"lion king\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f75a895e",
   "metadata": {},
   "outputs": [],
   "source": [
    "corpus = [D0,D1,D2,D3,q] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "1ce3ebdf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'discovery',\n",
       " 'fire',\n",
       " 'jungle',\n",
       " 'king',\n",
       " 'lion',\n",
       " 'mufasa',\n",
       " 'palace',\n",
       " 'simba',\n",
       " 'sleeps',\n",
       " 'timon'}"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "word_bag  = set(D0.split()+D1.split()+D2.split()+D3.split()+q.split())\n",
    "word_bag"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5bac00f6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['king palace jungle sleeps',\n",
       " 'jungle lion fire king discovery',\n",
       " 'king timon mufasa',\n",
       " 'timon lion simba',\n",
       " 'lion king']"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corpus"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "eb802359",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'discovery',\n",
       " 'fire',\n",
       " 'jungle',\n",
       " 'king',\n",
       " 'lion',\n",
       " 'mufasa',\n",
       " 'palace',\n",
       " 'simba',\n",
       " 'sleeps',\n",
       " 'timon'}"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "word_bag"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "08947c53",
   "metadata": {},
   "outputs": [],
   "source": [
    "doc = {'D0':\"king palace jungle sleeps\", 'D1':\"jungle lion fire king discovery\", 'D2':\"king timon mufasa\",'D3':\"timon lion simba\"}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "8f97c3b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "dict_doc = {'D0':\"king palace jungle sleeps\", 'D1':\"jungle lion fire king discovery\", 'D2':\"king timon mufasa\",'D3':\"timon lion simba\",'q':\"lion king\"}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "dba28f30",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['palace',\n",
       " 'fire',\n",
       " 'sleeps',\n",
       " 'lion',\n",
       " 'discovery',\n",
       " 'jungle',\n",
       " 'king',\n",
       " 'simba',\n",
       " 'mufasa',\n",
       " 'timon']"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "word_bag_list = list(word_bag)\n",
    "word_bag_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "6894428e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0.6020599913279623,\n",
       " 0.6020599913279623,\n",
       " 0.6020599913279623,\n",
       " 0.30102999566398114,\n",
       " 0.6020599913279623,\n",
       " 0.30102999566398114,\n",
       " 0.1249387366082999,\n",
       " 0.6020599913279623,\n",
       " 0.6020599913279623,\n",
       " 0.30102999566398114]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tf_word = {}\n",
    "for word in word_bag_list:\n",
    "    count = 0\n",
    "    for key in doc:\n",
    "        if(word in doc[key]):\n",
    "            count+=1\n",
    "            \n",
    "    tf_word[word] = math.log((4/count),10)\n",
    "\n",
    "list_tf = list(tf_word.values())\n",
    "list_tf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "64836ed4",
   "metadata": {},
   "outputs": [],
   "source": [
    "dict_doc_vectors = {}\n",
    "for key in dict_doc:\n",
    "    count = []\n",
    "    words_doc = dict_doc[key].split()\n",
    "    for word in word_bag_list:\n",
    "        count.append(words_doc.count(word))\n",
    "    dict_doc_vectors[key] = count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "713617f9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'D0': [1, 0, 0, 0, 1, 0, 0, 1, 1, 0],\n",
       " 'D1': [0, 1, 1, 0, 1, 1, 0, 0, 1, 0],\n",
       " 'D2': [0, 0, 0, 1, 0, 0, 0, 0, 1, 1],\n",
       " 'D3': [0, 0, 0, 1, 0, 1, 1, 0, 0, 0],\n",
       " 'q': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0]}"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dict_doc_vectors"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "6ee5a34c",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "docs_tf = {}\n",
    "for key in dict_doc_vectors:\n",
    "    docs_tf[key] = [a*b for a,b in zip(list_tf,dict_doc_vectors[key])]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "17ef0f7a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.0, 0.48164799306236983, 0.48164799306236983, 0, 0.24082399653118491, 0.511750992628768, 0, 0.0, 0.22488972589493983, 0.0]\n",
      "[0.0, 0.06020599913279623, 0.06020599913279623, 0, 0.030102999566398114, 0.06020599913279623, 0, 0.0, 0.1374326102691299, 0.0]\n",
      "[0.0, 0.6020599913279623, 0.6020599913279623, 0, 0.30102999566398114, 0.30102999566398114, 0, 0.0, 0.2498774732165998, 0.0]\n"
     ]
    }
   ],
   "source": [
    "def Rocchio(alpha, beta, gamma):\n",
    "    d = [a + b - c for a, b, c in zip([i * alpha for i in docs_tf['q']], [i * beta for i in docs_tf['D1']],  [i * gamma for i in docs_tf['D3']])]\n",
    "    for i in range(0,len(d)):\n",
    "        if d[i]<0:\n",
    "            d[i] = 0           \n",
    "    return d\n",
    "\n",
    "print(Rocchio(1,0.8,0.1))\n",
    "print(Rocchio(1,0.1,0.9))\n",
    "print(Rocchio(1,1,1))"
   ]
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
