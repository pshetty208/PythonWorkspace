{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "c908c433",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "a = np.array([[6/15, 5/15, 4/15],\n",
    "             [1/15,1/15,13/15],\n",
    "             [1/15,13/15,1/15]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "b7c12df0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(matrix([[0.33333333, 0.33333333, 0.33333333]]),\n",
       " matrix([[0.4       , 0.33333333, 0.26666667],\n",
       "         [0.06666667, 0.06666667, 0.86666667],\n",
       "         [0.06666667, 0.86666667, 0.06666667]]))"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = np.matrix(a)\n",
    "x0 = np.matrix([1/3,1/3,1/3])\n",
    "x0,a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "a1f583c6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "matrix([[0.10096022, 0.45425558, 0.4447842 ]])"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Values at 5th iteration\n",
    "x0*(a**5)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fc6420f0",
   "metadata": {},
   "source": [
    "How many iterations does it take for steady-state distribution values to converge? (Absolute difference values before and after iteration being less than or equal to 0.001)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "288b9e22",
   "metadata": {},
   "outputs": [],
   "source": [
    "a0 = x0*a**0\n",
    "a1 = x0*a**1\n",
    "a2 = x0*a**2\n",
    "a3 = x0*a**3\n",
    "a4 = x0*a**4\n",
    "a5 = x0*a**5\n",
    "a6 = x0*a**6\n",
    "a7 = x0*a**7\n",
    "a8 = x0*a**8\n",
    "a9 = x0*a**9\n",
    "a10 = x0*a**10\n",
    "a11 = x0*a**11\n",
    "a12 = x0*a**12\n",
    "a13 = x0*a**13\n",
    "a14 = x0*a**14\n",
    "a15 = x0*a**15"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "84dbfe26",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2 [[-0.05185185  0.01185185  0.04      ]] [[ True False False]]\n",
      "3 [[-0.01728395  0.01817284 -0.00088889]] [[ True False  True]]\n",
      "4 [[-0.00576132 -0.00532016  0.01108148]] [[ True  True False]]\n",
      "5 [[-0.00192044  0.00732883 -0.0054084 ]] [[ True False  True]]\n",
      "6 [[-0.00064015 -0.00483883  0.00547898]] [[ True  True False]]\n",
      "7 [[-0.00021338  0.00421248 -0.0039991 ]] [[ True False  True]]\n",
      "8 [[-7.11273688e-05 -3.25617849e-03  3.32730586e-03]] [[ True  True False]]\n",
      "9 [[-2.37091229e-05  2.64287739e-03 -2.61916827e-03]] [[ True False  True]]\n",
      "10 [[-7.90304098e-06 -2.10165705e-03  2.10956009e-03]] [[ True  True False]]\n",
      "11 [[-2.63434699e-06  1.68554059e-03 -1.68290625e-03]] [[ True False  True]]\n",
      "12 [[-8.78115664e-07 -1.34702749e-03  1.34790561e-03]] [[ True  True False]]\n",
      "13 [[-2.92705221e-07  1.07809032e-03 -1.07779761e-03]] [[ True False  True]]\n",
      "14 [[-9.75684071e-08 -8.62316146e-04  8.62413715e-04]] [[ True  True  True]]\n",
      "15 [[-3.25228024e-08  6.89904954e-04 -6.89872431e-04]] [[ True  True  True]]\n"
     ]
    }
   ],
   "source": [
    "#Convergence with iteration\n",
    "print(\"2\",a2-a1,a2-a1 <= [0.001,0.001,0.001])\n",
    "print(\"3\",a3-a2,a3-a2 <= [0.001,0.001,0.001])\n",
    "print(\"4\",a4-a3,a4-a3 <= [0.001,0.001,0.001])\n",
    "print(\"5\",a5-a4,a5-a4 <= [0.001,0.001,0.001])\n",
    "print(\"6\",a6-a5,a6-a5 <= [0.001,0.001,0.001])\n",
    "print(\"7\",a7-a6,a7-a6 <= [0.001,0.001,0.001])\n",
    "print(\"8\",a8-a7,a8-a7 <= [0.001,0.001,0.001])\n",
    "print(\"9\",a9-a8,a9-a8 <= [0.001,0.001,0.001])\n",
    "print(\"10\",a10-a9,a10-a9 <= [0.001,0.001,0.001])\n",
    "print(\"11\",a11-a10,a11-a10 <= [0.001,0.001,0.001])\n",
    "print(\"12\",a12-a11,a12-a11 <= [0.001,0.001,0.001])\n",
    "print(\"13\",a13-a12,a13-a12 <= [0.001,0.001,0.001])\n",
    "print(\"14\",a14-a13,a14-a13 <= [0.001,0.001,0.001])\n",
    "print(\"15\",a15-a14,a15-a14 <= [0.001,0.001,0.001])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "28f26e0c",
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
