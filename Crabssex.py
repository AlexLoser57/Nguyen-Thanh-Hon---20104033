{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AlexLoser57/Nguyen-Thanh-Hon---20104033/blob/main/Crabssex.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Tq7KqFplvlxE",
        "outputId": "748c4244-c12b-4443-e8c6-4e5eb5595ae5"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Do chinh xac 0.5\n",
            "sex:  ['M']\n"
          ]
        }
      ],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "from sklearn.linear_model import Perceptron\n",
        "from sklearn.model_selection import train_test_split\n",
        "\n",
        "crab = 'crabs.csv'\n",
        "crab_data = pd.read_csv(crab)\n",
        "data = (crab_data.drop('speies', axis=1)).drop('index', axis=1)\n",
        "\n",
        "\n",
        "\n",
        "x_train = [data['fontallip'], data['rearwidth'],data['length'], data['width'], data['depth']]\n",
        "y_train = data['sex']\n",
        "\n",
        "x = np.reshape(x_train, (200, 5))\n",
        "y = np.reshape(y_train, (200))\n",
        "\n",
        "data.replace('M', 0)\n",
        "data.replace('F', 1)\n",
        "\n",
        "model = Perceptron()\n",
        "\n",
        "model.fit(x, y)\n",
        "\n",
        "print('Do chinh xac', model.score(x, y))\n",
        "\n",
        "x_test = [[11.7, 10.6, 24.9, 28.5, 10.4]]\n",
        "y_test = model.predict(x_test)\n",
        "print('sex: ', y_test)\n"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyNMIKEB6Z+zZzi6SFv6S6cd",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}