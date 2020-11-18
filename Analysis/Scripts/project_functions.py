{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "def load_and_process(url_or_path_to_csv_file):\n",
    "\n",
    "    # Method Chain 1 (Load data and deal with missing data)\n",
    "\n",
    "    df1 = (\n",
    "          pd.read_csv(url_or_path_to_csv_file).dropna()\n",
    "          .rename(columns={\"id\": \"Property_id\"})\n",
    "          .rename(columns={\"name\": \"Property_name\"})                 \n",
    "        \n",
    "        .reset_index(drop=True)\n",
    "          # etc...\n",
    "      )\n",
    "\n",
    "    # Method Chain 2 (Create new columns, drop others, and do processing)\n",
    "\n",
    "    df2 = (\n",
    "          df1\n",
    "          \n",
    "          .sort_values(\"price\", ascending=True)\n",
    "          .drop(columns=['Longitude', 'Latitude'])\n",
    "          .drop(columns=['Neighbuorhood_group'])\n",
    "      )\n",
    "    \n",
    "    \n",
    "\n",
    "    # Make sure to return the latest dataframe\n",
    "    \n",
    "    return df2"
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
