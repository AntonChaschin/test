{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input number:4652\n"
     ]
    }
   ],
   "source": [
    "moment = int(input(\"Input number:\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "result = 26:3\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Введенное число превышает количество минут в сутках, желательно введение числа не превышающего значения 1440\n",
      "С учетом введенных данных с момента отсчета времени прошло None\n"
     ]
    }
   ],
   "source": [
    "\n",
    "    print (\"С учетом введенных данных с момента отсчета времени прошло\",  result ) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Введенное число превышает количество минут в сутках, желательно введение числа не превышающего значения 1440\n",
      "С момента отсчета времени прошло более 3 дней\n"
     ]
    }
   ],
   "source": [
    "if moment <= 1440:\n",
    "    a = moment // 60\n",
    "    b = moment % 60\n",
    "    if a < 10:        \n",
    "        if b < 10:\n",
    "            result = \"0\" + str(a) + \":\" + \"0\" + str(b)\n",
    "            print(\"result =\", result)\n",
    "    else:\n",
    "        result = str(a) + \":\" + str(b)\n",
    "        print(\"result =\",result)\n",
    "else:\n",
    "    c = moment // 1440\n",
    "    print (\"Введенное число превышает количество минут в сутках, желательно введение числа не превышающего значения 1440\")\n",
    "    print (\"С момента отсчета времени прошло более\", str(c) + \" дней\")\n",
    "    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
