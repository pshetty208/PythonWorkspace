{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ce58c127",
   "metadata": {},
   "source": [
    "Create following functions : \n",
    "\n",
    "def precision(matrix)\n",
    "It calculates precision, where the input is a matrix that consists of two columns (the retrieved class, the gold standard).\n",
    "\n",
    "def recall(matrix) \n",
    "It calculates recall, where the input is a matrix that consists of two columns (the retrieved class, the gold standard)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "a0ad3701",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Precision  0  : 1.0\n",
      "Precision  1  : 0.7894736842105263\n",
      "Precision  2  : 1.0\n",
      "Recall  0  : 1.0\n",
      "Recall  1  : 1.0\n",
      "Recall  2  : 0.6363636363636364\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "    \n",
    "a = np.array(([19, 0,0], [0, 15,0], [0, 4, 7]))\n",
    "pr = [0,0,0]\n",
    "rc = [0,0,0]\n",
    "\n",
    "def precision(a):\n",
    "    for i in range(len(a)): \n",
    "        fp = 0\n",
    "        tp = a[i][i]\n",
    "        for j in range(len(a)):\n",
    "            if(i!=j):\n",
    "                fp = fp + a[j][i]\n",
    "        p = tp/(tp + fp)\n",
    "        print(\"Precision \",i,\" :\" , p)\n",
    "        pr[i] = p\n",
    "\n",
    "def recall(a): \n",
    "    for i in range(len(a)): \n",
    "        fn = 0 \n",
    "        tp = a[i][i]\n",
    "        for j in range(len(a)):\n",
    "            if(i!=j):\n",
    "                fn = fn + a[i][j]\n",
    "        r = tp/(tp+fn)\n",
    "        print(\"Recall \",i,\" :\", r)\n",
    "        rc[i] = r\n",
    "        \n",
    "precision(a)\n",
    "recall(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "2a350866",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Precision for element  0  : 1.0\n",
      "Precision for element  1  : 0.7894736842105263\n",
      "Precision for element  2  : 1.0\n",
      "Recall for element  0  : 1.0\n",
      "Recall for element  1  : 1.0\n",
      "Recall for element  2  : 0.6363636363636364\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "    \n",
    "a = np.array(([19, 0,0], [0, 15,0], [0, 4, 7]))\n",
    "\n",
    "def precision(matrix):\n",
    "\tfor i in range(len(matrix)):\n",
    "\t\tfp = 0\n",
    "\t\ttp = matrix[i][i]\n",
    "\t\tfor j in range(len(matrix)):\n",
    "\t\t\tif(i!=j):\n",
    "\t\t\t\tfp=fp+matrix[j][i]\n",
    "\t\tp = tp/(tp + fp)\n",
    "\t\tprint(\"Precision for element \",i,\" :\", p)\n",
    "\n",
    "def recall(matrix): \n",
    "\tfor i in range(len(matrix)):\n",
    "\t\tfn = 0\n",
    "\t\ttp = matrix[i][i]\n",
    "\t\tfor j in range(len(matrix)):\n",
    "\t\t\tif(i!=j):\n",
    "\t\t\t\tfn=fn+matrix[i][j]\n",
    "\t\tr = tp/(tp + fn)\n",
    "\t\tprint(\"Recall for element \",i,\" :\", r)\n",
    "\n",
    "precision(a)\n",
    "recall(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "00663f55",
   "metadata": {},
   "source": [
    "Complete the following confusion matrix from the dataset provided."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1c63d561",
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
       "      <th>retrieved</th>\n",
       "      <th>gold_standard</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>setosa</td>\n",
       "      <td>setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>setosa</td>\n",
       "      <td>setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>setosa</td>\n",
       "      <td>setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>versicolor</td>\n",
       "      <td>versicolor</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>setosa</td>\n",
       "      <td>setosa</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    retrieved gold_standard\n",
       "0      setosa        setosa\n",
       "1      setosa        setosa\n",
       "2      setosa        setosa\n",
       "3  versicolor    versicolor\n",
       "4      setosa        setosa"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv(\"Iris.csv\")\n",
    "\n",
    "df.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "cc61b065",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['retrieved', 'gold_standard'], dtype='object')"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "02566d5b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "gold_standard  retrieved \n",
       "setosa         setosa        19\n",
       "versicolor     versicolor    15\n",
       "               virginica      4\n",
       "virginica      virginica      7\n",
       "dtype: int64"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby(['gold_standard','retrieved']).size()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "53b3bcdf",
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
       "      <th>gold_standard</th>\n",
       "      <th>retrieved</th>\n",
       "      <th>counts</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>setosa</td>\n",
       "      <td>setosa</td>\n",
       "      <td>19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>versicolor</td>\n",
       "      <td>versicolor</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>versicolor</td>\n",
       "      <td>virginica</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>virginica</td>\n",
       "      <td>virginica</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  gold_standard   retrieved  counts\n",
       "0        setosa      setosa      19\n",
       "1    versicolor  versicolor      15\n",
       "2    versicolor   virginica       4\n",
       "3     virginica   virginica       7"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby(['gold_standard','retrieved']).size().reset_index(name='counts')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "feed7b47",
   "metadata": {},
   "source": [
    "Calculate the precision of each of the following classes:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "0ab54faa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Precision  0  : 1.0\n",
      "Precision  1  : 0.79\n",
      "Precision  2  : 1.0\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "a = np.array(([19, 0,0], [0, 15,0], [0, 4, 7]))\n",
    "\n",
    "def precision(a):\n",
    "    for i in range(len(a)): \n",
    "        fp = 0\n",
    "        tp = a[i][i]\n",
    "        for j in range(len(a)):\n",
    "            if(i!=j):\n",
    "                fp = fp + a[j][i]\n",
    "        p = tp/(tp + fp)\n",
    "        print(\"Precision \",i,\" :\" , round(p,2))\n",
    "        \n",
    "precision(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0dbd8dd3",
   "metadata": {},
   "source": [
    "Calculate the recall of each of the following classes:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "4550a8e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Recall  0  : 1.0\n",
      "Recall  1  : 1.0\n",
      "Recall  2  : 0.64\n"
     ]
    }
   ],
   "source": [
    "def recall(a): \n",
    "    for i in range(len(a)): \n",
    "        fn = 0 \n",
    "        tp = a[i][i]\n",
    "        for j in range(len(a)):\n",
    "            if(i!=j):\n",
    "                fn = fn + a[i][j]\n",
    "        r = tp/(tp+fn)\n",
    "        print(\"Recall \",i,\" :\", round(r,2))\n",
    "        \n",
    "recall(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ae823c8e",
   "metadata": {},
   "source": [
    "Calculate the F1-score of each of the following classes:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "a9ce47db",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Precision  0  : 1.0\n",
      "Precision  1  : 0.7894736842105263\n",
      "Precision  2  : 1.0\n",
      "Recall  0  : 1.0\n",
      "Recall  1  : 1.0\n",
      "Recall  2  : 0.6363636363636364\n",
      "f1 for  0  =  1.0\n",
      "f1 for  1  =  0.8823529411764706\n",
      "f1 for  2  =  0.7777777777777778\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "    \n",
    "a = np.array(([19, 0,0], [0, 15,0], [0, 4, 7]))\n",
    "pr = [0,0,0]\n",
    "rc = [0,0,0]\n",
    "\n",
    "def precision(a):\n",
    "    for i in range(len(a)): \n",
    "        fp = 0\n",
    "        tp = a[i][i]\n",
    "        for j in range(len(a)):\n",
    "            if(i!=j):\n",
    "                fp = fp + a[j][i]\n",
    "        p = tp/(tp + fp)\n",
    "        print(\"Precision \",i,\" :\" , p)\n",
    "        pr[i] = p\n",
    "\n",
    "def recall(a): \n",
    "    for i in range(len(a)): \n",
    "        fn = 0 \n",
    "        tp = a[i][i]\n",
    "        for j in range(len(a)):\n",
    "            if(i!=j):\n",
    "                fn = fn + a[i][j]\n",
    "        r = tp/(tp+fn)\n",
    "        print(\"Recall \",i,\" :\", r)\n",
    "        rc[i] = r\n",
    "        \n",
    "precision(a)\n",
    "recall(a)\n",
    "for i in range(len(a)):\n",
    "    print(\"f1 for \",i,\" = \",(2*pr[i]*rc[i])/(pr[i]+rc[i]))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1757546a",
   "metadata": {},
   "source": [
    "Calculate the precision @ \"10\" of each of the following classes:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "8b32b12f",
   "metadata": {},
   "outputs": [],
   "source": [
    "mewdf = df.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "1803a4b5",
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
       "      <th>retrieved</th>\n",
       "      <th>gold_standard</th>\n",
       "      <th>counts</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>setosa</td>\n",
       "      <td>setosa</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>versicolor</td>\n",
       "      <td>versicolor</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>virginica</td>\n",
       "      <td>versicolor</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    retrieved gold_standard  counts\n",
       "0      setosa        setosa       7\n",
       "1  versicolor    versicolor       2\n",
       "2   virginica    versicolor       1"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mewdf.groupby(['retrieved','gold_standard']).size().reset_index(name='counts')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "c36e3a1f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Precision  0  : 1.0\n",
      "Precision  1  : 0.6666666666666666\n",
      "Precision  2  : nan\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\PRAJNA~1\\AppData\\Local\\Temp/ipykernel_5164/4038234539.py:14: RuntimeWarning: invalid value encountered in long_scalars\n",
      "  p = tp/(tp + fp)\n"
     ]
    }
   ],
   "source": [
    "a = np.array(([7, 0,0], [0, 2,0], [0, 1, 0]))\n",
    "\n",
    "precision(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a54c280d",
   "metadata": {},
   "source": [
    "Calculate the accuracy of the retrieval system:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "4f5a407f",
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
       "      <th>retrieved</th>\n",
       "      <th>gold_standard</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>45</td>\n",
       "      <td>45</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>unique</th>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>top</th>\n",
       "      <td>setosa</td>\n",
       "      <td>setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>freq</th>\n",
       "      <td>19</td>\n",
       "      <td>19</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       retrieved gold_standard\n",
       "count         45            45\n",
       "unique         3             3\n",
       "top       setosa        setosa\n",
       "freq          19            19"
      ]
     },
     "execution_count": 64,
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
   "execution_count": null,
   "id": "a27942c6",
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
