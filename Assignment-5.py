{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Query history\n",
    "\n",
    "•𝑞0= the weather forecast in Koblenz\n",
    "\n",
    "•𝑞1= next week weather forecast\n",
    "\n",
    "•𝑞2= the weather tomorrow\n",
    "\n",
    "•𝑞3= weather forecast Amsterdam\n",
    "\n",
    "•𝑞4= the weather tomorrow in"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Possible auto-complete outcomes i.e., words following ”the weather” in the query history 𝑎𝑖:\n",
    "\n",
    "                                 •𝑎1=the weather the\n",
    "                                 •𝑎2=the weather weather\n",
    "                                 •𝑎3=the weather forecast\n",
    "                                 •𝑎4=the weather in\n",
    "                                 •𝑎5=the weather Koblenz\n",
    "                                 •𝑎6=the weather next\n",
    "                                 •𝑎7=the weather week\n",
    "                                 •𝑎8=the weather tomorrow\n",
    "                                 •𝑎9=the weather Amsterdam\n",
    "                                 \n",
    "Let 𝒟 be the corpus of all queries from the history"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Vocab = {the weather forecast in koblenz next week tomorrow Amsterdam}"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Bigram Model\n",
    "𝑃bi(𝑡1 𝑡2 𝑡3) =𝑃(𝑡1)𝑃(𝑡2/𝑡1)𝑃(𝑡3/𝑡2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "𝒫𝑏𝑖(the weather forecast)\n",
    "\n",
    "=𝒫𝑢𝑛𝑖(𝑡ℎ𝑒)×𝒫𝑏𝑖(𝑤𝑒𝑎𝑡ℎ𝑒𝑟|𝑡ℎ𝑒)×𝒫𝑏𝑖(𝑓𝑜𝑟𝑒𝑐𝑎𝑠𝑡|𝑤𝑒𝑎𝑡ℎ𝑒𝑟)\n",
    "\n",
    "=𝑡𝑓(𝑡ℎ𝑒,𝐷)/𝑑𝑙(𝐷) × 𝑡𝑓((𝑡ℎ𝑒,𝑤𝑒𝑎𝑡ℎ𝑒𝑟),𝐷)/𝑑𝑙(𝑡ℎ𝑒,𝐷) × 𝑡𝑓((𝑤𝑒𝑎𝑡ℎ𝑒𝑟,𝑓𝑜𝑟𝑒𝑐𝑎𝑠𝑡), 𝐷)/𝑑𝑙(𝑤𝑒𝑎𝑡ℎ𝑒𝑟,𝐷)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Trigram Model\n",
    "\n",
    "𝑃tri(𝑡1 𝑡2 𝑡3) =𝑃(𝑡1)𝑃(𝑡2/𝑡1)𝑃(𝑡3/𝑡1, 𝑡2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "𝒫𝑡𝑟𝑖(the weather tomorrow)\n",
    "\n",
    "= 𝒫𝑢𝑛𝑖(𝑡ℎ𝑒)×𝒫𝑏𝑖(𝑤𝑒𝑎𝑡ℎ𝑒𝑟|𝑡ℎ𝑒)×𝒫𝑡𝑟𝑖(𝑡𝑜𝑚𝑜𝑟𝑟𝑜𝑤|𝑡ℎ𝑒𝑤𝑒𝑎𝑡ℎ𝑒𝑟)\n",
    "\n",
    "=𝑡𝑓(𝑡ℎ𝑒,𝐷)/𝑑𝑙(𝐷) × 𝑡𝑓((𝑡ℎ𝑒,𝑤𝑒𝑎𝑡ℎ𝑒𝑟),𝐷)/𝑑𝑙(𝑡ℎ𝑒,𝐷) × 𝑡𝑓((𝑡ℎ𝑒,𝑤𝑒𝑎𝑡ℎ𝑒𝑟,𝑡𝑜𝑚𝑜𝑟𝑟𝑜𝑤),𝐷)/𝑑𝑙((the weather),𝐷)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import operator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "D1='vaccine research corona virus research'\n",
    "D2='research research cancer vaccine vaccine'\n",
    "D3= 'virus virus corona vaccine lab'\n",
    "D4= 'cancer lab research lab'\n",
    "\n",
    "#q = 'vaccine vaccine research cancer'\n",
    "corpus=[D1,D2,D3,D4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['vaccine', 'research', 'corona', 'virus', 'research']"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "D1.split()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "word_bag= set(D1.split()+D2.split()+D3.split()+D4.split())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'cancer', 'corona', 'lab', 'research', 'vaccine', 'virus'}"
      ]
     },
     "execution_count": 5,
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
   "execution_count": 6,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#𝑇 is the number of tokens in the whole collection\n",
    "T= len(D1.split())+len(D2.split())+len(D3.split())+len(D4.split())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "19"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "T"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1-calcualting the probability of a term appearing in the whole corpus\n",
    "## ${P_{M}}_c(t)= \\frac{cf(t))}{T}$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'corona': 0.10526315789473684,\n",
       " 'cancer': 0.10526315789473684,\n",
       " 'virus': 0.15789473684210525,\n",
       " 'vaccine': 0.21052631578947367,\n",
       " 'research': 0.2631578947368421,\n",
       " 'lab': 0.15789473684210525}"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#P_Mc is the probability of a term appearing in the whole corpus\n",
    "cf={} # is for counting the corpus frequency\n",
    "P_Mc={}\n",
    "for term in word_bag:\n",
    "    for doc in corpus: ##here I am counting the number of each term in whole corpus\n",
    "        if term in cf.keys():\n",
    "            cf[term]+=doc.count(term) \n",
    "        else:\n",
    "            cf[term]= doc.count(term)\n",
    "           \n",
    "    P_Mc[term]=cf[term]/T # getting the probability of term by dividing it to the number of tokens in the whole collection\n",
    "\n",
    "P_Mc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0.10526315789473684,\n",
       " 0.10526315789473684,\n",
       " 0.15789473684210525,\n",
       " 0.15789473684210525,\n",
       " 0.21052631578947367,\n",
       " 0.2631578947368421]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(sorted(P_Mc.values()))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2- Calcualting the probability of a term 𝑡 occurring in document 𝑑\n",
    "## ${P_{M}}_d(t)= \\frac{tf(t,d))}{dl}$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'vaccine research corona virus research'"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "D1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
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
       "      <th>D1</th>\n",
       "      <th>D2</th>\n",
       "      <th>D3</th>\n",
       "      <th>D4</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>corona</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>cancer</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>virus</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>vaccine</th>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>research</th>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>lab</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         D1 D2 D3 D4\n",
       "corona    1  0  1  0\n",
       "cancer    0  1  0  1\n",
       "virus     1  0  2  0\n",
       "vaccine   1  2  1  0\n",
       "research  2  2  0  1\n",
       "lab       0  0  1  2"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#P_Md is a dataframe for the probability of term 𝑡 occurring in document 𝑑\n",
    "\n",
    "P_Md=pd.DataFrame(index=list(word_bag),columns=['D1','D2','D3','D4'])\n",
    "\n",
    "#each doc is a column and each index is a term \n",
    "for term in word_bag:\n",
    "    for doc,col in zip(corpus,P_Md.columns):\n",
    "               \n",
    "        P_Md[col][term]= doc.count(term)\n",
    "P_Md"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "tags": []
   },
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
       "      <th>D1</th>\n",
       "      <th>D2</th>\n",
       "      <th>D3</th>\n",
       "      <th>D4</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>corona</th>\n",
       "      <td>0.2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>cancer</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>virus</th>\n",
       "      <td>0.2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.4</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>vaccine</th>\n",
       "      <td>0.2</td>\n",
       "      <td>0.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>research</th>\n",
       "      <td>0.4</td>\n",
       "      <td>0.4</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>lab</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0.5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           D1   D2   D3    D4\n",
       "corona    0.2  0.0  0.2   0.0\n",
       "cancer    0.0  0.2  0.0  0.25\n",
       "virus     0.2  0.0  0.4   0.0\n",
       "vaccine   0.2  0.4  0.2   0.0\n",
       "research  0.4  0.4  0.0  0.25\n",
       "lab       0.0  0.0  0.2   0.5"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "for term in word_bag:\n",
    "    for doc,col in zip(corpus,P_Md.columns):       \n",
    "        P_Md[col][term]= doc.count(term)/len(doc.split()) #probability of each term in a doc is number of times term \n",
    "                                                            #occured divided by document length\n",
    "P_Md"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
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
       "      <th>D1</th>\n",
       "      <th>D2</th>\n",
       "      <th>D3</th>\n",
       "      <th>D4</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>cancer</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>corona</th>\n",
       "      <td>0.2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>lab</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>research</th>\n",
       "      <td>0.4</td>\n",
       "      <td>0.4</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>vaccine</th>\n",
       "      <td>0.2</td>\n",
       "      <td>0.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>virus</th>\n",
       "      <td>0.2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.4</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           D1   D2   D3    D4\n",
       "cancer    0.0  0.2  0.0  0.25\n",
       "corona    0.2  0.0  0.2   0.0\n",
       "lab       0.0  0.0  0.2   0.5\n",
       "research  0.4  0.4  0.0  0.25\n",
       "vaccine   0.2  0.4  0.2   0.0\n",
       "virus     0.2  0.0  0.4   0.0"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "P_Md = P_Md.sort_index()\n",
    "P_Md"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.2, 0.4, 0.2, 0.0], dtype=object)"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "P_Md.loc['vaccine'].values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3- Calculating the ranked result set according to the unsmoothed, uniform model\n",
    "## $P_{uni}(d|q)=\\prod_{t\\varepsilon q}^{}{P_{M}}_d(t)$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "q = 'vaccine vaccine research cancer'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'D1': 0.0, 'D2': 0.012800000000000004, 'D3': 0.0, 'D4': 0.0} \n",
      "\n",
      "\n",
      "[('D2', 0.012800000000000004), ('D1', 0.0), ('D3', 0.0), ('D4', 0.0)]\n"
     ]
    }
   ],
   "source": [
    "#P_uni is the result set according to the unsmoothed, uniform model\n",
    "P_uni={}\n",
    "\n",
    "for col in P_Md.columns:\n",
    "    P_uni[col]=1\n",
    "    for term in q.split():  \n",
    "      \n",
    "        P_uni[col]= P_Md[col][term]*P_uni[col] #the unigram model is the multiplication of unigram probability of terms(in q) \n",
    "                                                ##that we found them in the previous cell\n",
    "\n",
    "print(P_uni,\"\\n\\n\")\n",
    "sorted_P_uni = sorted(P_uni.items(), key=operator.itemgetter(1), reverse=True)\n",
    "print(sorted_P_uni)\n",
    "\n",
    "# P(D1/q) = 0.2*0.2*0.4*0 = 0 \n",
    "# P(D2/q) = 0.4*0.4*0.4*0.2 = 0.0128\n",
    "# P(D3/q) = 0.2*0.2*0*0 = 0\n",
    "# P(D4/q) = 0*0*0.25*0.25 =0\n",
    "\n",
    "# Rank D2> (D1=D3=D4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'D1': 0.0007352844131030303,\n",
       " 'D2': 0.004716068784002579,\n",
       " 'D3': 0.000291779529009139,\n",
       " 'D4': 0.0005050030309773557}"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#P_interp is the result set according to the linear-interpolated, uniform model\n",
    "P_interp={}\n",
    "lamb=0.5\n",
    "\n",
    "for col in P_Md.columns:\n",
    "    P_interp[col]=1\n",
    "    for term in q.split():      \n",
    "        P_interp[col]= ((lamb*P_Md[col][term])+((1-lamb)*P_Mc[term]))*P_interp[col]\n",
    "        \n",
    "P_interp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('D2', 0.004716068784002579),\n",
       " ('D1', 0.0007352844131030303),\n",
       " ('D4', 0.0005050030309773557),\n",
       " ('D3', 0.000291779529009139)]"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sorted_P_interp = sorted(P_interp.items(), key=operator.itemgetter(1), reverse=True)\n",
    "sorted_P_interp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0.0047, 0.0007, 0.0005, 0.0003]"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[round(i,4) for i in (sorted(P_interp.values(), reverse=True))]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'corona': 0.10526315789473684,\n",
       " 'cancer': 0.10526315789473684,\n",
       " 'virus': 0.15789473684210525,\n",
       " 'vaccine': 0.21052631578947367,\n",
       " 'research': 0.2631578947368421,\n",
       " 'lab': 0.15789473684210525}"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "P_Mc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
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
       "      <th>D1</th>\n",
       "      <th>D2</th>\n",
       "      <th>D3</th>\n",
       "      <th>D4</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>cancer</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>corona</th>\n",
       "      <td>0.2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>lab</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>research</th>\n",
       "      <td>0.4</td>\n",
       "      <td>0.4</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>vaccine</th>\n",
       "      <td>0.2</td>\n",
       "      <td>0.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>virus</th>\n",
       "      <td>0.2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.4</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           D1   D2   D3    D4\n",
       "cancer    0.0  0.2  0.0  0.25\n",
       "corona    0.2  0.0  0.2   0.0\n",
       "lab       0.0  0.0  0.2   0.5\n",
       "research  0.4  0.4  0.0  0.25\n",
       "vaccine   0.2  0.4  0.2   0.0\n",
       "virus     0.2  0.0  0.4   0.0"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "P_Md"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "q='vaccine research'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'D1': 0.08000000000000002, 'D2': 0.16000000000000003, 'D3': 0.0, 'D4': 0.0} \n",
      "\n",
      "\n",
      "[('D2', 0.16000000000000003), ('D1', 0.08000000000000002), ('D3', 0.0), ('D4', 0.0)]\n"
     ]
    }
   ],
   "source": [
    "P_uni={}\n",
    "\n",
    "for col in P_Md.columns:\n",
    "    P_uni[col]=1\n",
    "    for term in q.split():  \n",
    "      \n",
    "        P_uni[col]= P_Md[col][term]*P_uni[col] #the unigram model is the multiplication of unigram probability of terms(in q) \n",
    "                                                ##that we found them in the previous cell\n",
    "\n",
    "print(P_uni,\"\\n\\n\")\n",
    "sorted_P_uni = sorted(P_uni.items(), key=operator.itemgetter(1), reverse=True)\n",
    "print(sorted_P_uni)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'D1': 0.06806094182825485,\n",
       " 'D2': 0.10121883656509696,\n",
       " 'D3': 0.027008310249307478,\n",
       " 'D4': 0.027008310249307475}"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "P_interp={}\n",
    "lamb=0.5\n",
    "\n",
    "for col in P_Md.columns:\n",
    "    P_interp[col]=1\n",
    "    for term in q.split():      \n",
    "        P_interp[col]= ((lamb*P_Md[col][term])+((1-lamb)*P_Mc[term]))*P_interp[col]\n",
    "        \n",
    "P_interp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('D2', 0.10121883656509696),\n",
       " ('D1', 0.06806094182825485),\n",
       " ('D3', 0.027008310249307478),\n",
       " ('D4', 0.027008310249307475)]"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sorted_P_interp = sorted(P_interp.items(), key=operator.itemgetter(1), reverse=True)\n",
    "sorted_P_interp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0.027, 0.027, 0.0681, 0.1012]"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[round(i,4) for i in (sorted(P_interp.values()))]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
 "nbformat_minor": 4
}
