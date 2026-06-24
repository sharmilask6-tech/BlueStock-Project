{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "58ab645f-b51f-4912-9a19-ab735d057acb",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "df=pd.read_csv(\"01_fund_master.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "35139ea5-6cf2-4ae3-9ea3-fa38e264a55e",
   "metadata": {},
   "outputs": [],
   "source": [
    "df1=pd.read_csv(\"02_nav_history.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "59d1113e-6e14-49dc-bc00-d268b28039c9",
   "metadata": {},
   "outputs": [],
   "source": [
    "df2=pd.read_csv(\"03_aum_by_fund_house.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "7448c756-34d8-469a-a297-80f2eb754354",
   "metadata": {},
   "outputs": [],
   "source": [
    "df3=pd.read_csv(\"04_monthly_sip_inflows.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "9662c031-4b81-48bc-b8d5-48a89bdb139b",
   "metadata": {},
   "outputs": [],
   "source": [
    "df4=pd.read_csv(\"05_category_inflows.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "a5c4835f-80ab-41bc-8735-398689d87a6b",
   "metadata": {},
   "outputs": [],
   "source": [
    "df5=pd.read_csv(\"06_industry_folio_count.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "fd4dca0f-e83d-402a-a26b-9a524887a41c",
   "metadata": {},
   "outputs": [],
   "source": [
    "df6=pd.read_csv(\"07_scheme_performance.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "3291b83e-ef27-474f-9abf-b84568aeaa03",
   "metadata": {},
   "outputs": [],
   "source": [
    "df7=pd.read_csv(\"08_investor_transactions.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "df301efe-e88c-4543-b0a1-6a06e69aa231",
   "metadata": {},
   "outputs": [],
   "source": [
    "df8=pd.read_csv(\"09_portfolio_holdings.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "c90060a8-91f7-4bf9-9b56-da15d4057d0a",
   "metadata": {},
   "outputs": [],
   "source": [
    "df9=pd.read_csv(\"10_benchmark_indices.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "0a45eda8-6909-4ef9-b705-234d5cc625ae",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(40, 15)\n"
     ]
    }
   ],
   "source": [
    "print(df.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "a512c747-5a8b-4c22-b99f-1351e62d6b6a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "amfi_code               int64\n",
      "fund_house             object\n",
      "scheme_name            object\n",
      "category               object\n",
      "sub_category           object\n",
      "plan                   object\n",
      "launch_date            object\n",
      "benchmark              object\n",
      "expense_ratio_pct     float64\n",
      "exit_load_pct         float64\n",
      "min_sip_amount          int64\n",
      "min_lumpsum_amount      int64\n",
      "fund_manager           object\n",
      "risk_category          object\n",
      "sebi_category_code     object\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "print(df.dtypes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "5760fee2-bea5-4762-869f-3e67a9a30f53",
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
       "      <th>amfi_code</th>\n",
       "      <th>fund_house</th>\n",
       "      <th>scheme_name</th>\n",
       "      <th>category</th>\n",
       "      <th>sub_category</th>\n",
       "      <th>plan</th>\n",
       "      <th>launch_date</th>\n",
       "      <th>benchmark</th>\n",
       "      <th>expense_ratio_pct</th>\n",
       "      <th>exit_load_pct</th>\n",
       "      <th>min_sip_amount</th>\n",
       "      <th>min_lumpsum_amount</th>\n",
       "      <th>fund_manager</th>\n",
       "      <th>risk_category</th>\n",
       "      <th>sebi_category_code</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>119551</td>\n",
       "      <td>SBI Mutual Fund</td>\n",
       "      <td>SBI Bluechip Fund - Regular Plan - Growth</td>\n",
       "      <td>Equity</td>\n",
       "      <td>Large Cap</td>\n",
       "      <td>Regular</td>\n",
       "      <td>2006-02-14</td>\n",
       "      <td>NIFTY 100 TRI</td>\n",
       "      <td>1.54</td>\n",
       "      <td>1.0</td>\n",
       "      <td>500</td>\n",
       "      <td>1000</td>\n",
       "      <td>Sohini Andani</td>\n",
       "      <td>Moderate</td>\n",
       "      <td>EC01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>119552</td>\n",
       "      <td>SBI Mutual Fund</td>\n",
       "      <td>SBI Bluechip Fund - Direct Plan - Growth</td>\n",
       "      <td>Equity</td>\n",
       "      <td>Large Cap</td>\n",
       "      <td>Direct</td>\n",
       "      <td>2013-01-01</td>\n",
       "      <td>NIFTY 100 TRI</td>\n",
       "      <td>0.66</td>\n",
       "      <td>1.0</td>\n",
       "      <td>500</td>\n",
       "      <td>1000</td>\n",
       "      <td>Sohini Andani</td>\n",
       "      <td>Moderate</td>\n",
       "      <td>EC01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>119598</td>\n",
       "      <td>SBI Mutual Fund</td>\n",
       "      <td>SBI Small Cap Fund - Regular Plan - Growth</td>\n",
       "      <td>Equity</td>\n",
       "      <td>Small Cap</td>\n",
       "      <td>Regular</td>\n",
       "      <td>2009-09-09</td>\n",
       "      <td>BSE 250 SmallCap TRI</td>\n",
       "      <td>1.43</td>\n",
       "      <td>1.0</td>\n",
       "      <td>500</td>\n",
       "      <td>1000</td>\n",
       "      <td>R. Srinivasan</td>\n",
       "      <td>Very High</td>\n",
       "      <td>EC03</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>119599</td>\n",
       "      <td>SBI Mutual Fund</td>\n",
       "      <td>SBI Small Cap Fund - Direct Plan - Growth</td>\n",
       "      <td>Equity</td>\n",
       "      <td>Small Cap</td>\n",
       "      <td>Direct</td>\n",
       "      <td>2013-01-01</td>\n",
       "      <td>BSE 250 SmallCap TRI</td>\n",
       "      <td>0.72</td>\n",
       "      <td>1.0</td>\n",
       "      <td>500</td>\n",
       "      <td>1000</td>\n",
       "      <td>R. Srinivasan</td>\n",
       "      <td>Very High</td>\n",
       "      <td>EC03</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>119120</td>\n",
       "      <td>SBI Mutual Fund</td>\n",
       "      <td>SBI Magnum Gilt Fund - Regular Plan - Growth</td>\n",
       "      <td>Debt</td>\n",
       "      <td>Gilt</td>\n",
       "      <td>Regular</td>\n",
       "      <td>2000-12-30</td>\n",
       "      <td>CRISIL Dynamic Gilt Index</td>\n",
       "      <td>0.77</td>\n",
       "      <td>0.0</td>\n",
       "      <td>500</td>\n",
       "      <td>1000</td>\n",
       "      <td>Dinesh Ahuja</td>\n",
       "      <td>Low</td>\n",
       "      <td>DC02</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   amfi_code       fund_house                                   scheme_name  \\\n",
       "0     119551  SBI Mutual Fund     SBI Bluechip Fund - Regular Plan - Growth   \n",
       "1     119552  SBI Mutual Fund      SBI Bluechip Fund - Direct Plan - Growth   \n",
       "2     119598  SBI Mutual Fund    SBI Small Cap Fund - Regular Plan - Growth   \n",
       "3     119599  SBI Mutual Fund     SBI Small Cap Fund - Direct Plan - Growth   \n",
       "4     119120  SBI Mutual Fund  SBI Magnum Gilt Fund - Regular Plan - Growth   \n",
       "\n",
       "  category sub_category     plan launch_date                  benchmark  \\\n",
       "0   Equity    Large Cap  Regular  2006-02-14              NIFTY 100 TRI   \n",
       "1   Equity    Large Cap   Direct  2013-01-01              NIFTY 100 TRI   \n",
       "2   Equity    Small Cap  Regular  2009-09-09       BSE 250 SmallCap TRI   \n",
       "3   Equity    Small Cap   Direct  2013-01-01       BSE 250 SmallCap TRI   \n",
       "4     Debt         Gilt  Regular  2000-12-30  CRISIL Dynamic Gilt Index   \n",
       "\n",
       "   expense_ratio_pct  exit_load_pct  min_sip_amount  min_lumpsum_amount  \\\n",
       "0               1.54            1.0             500                1000   \n",
       "1               0.66            1.0             500                1000   \n",
       "2               1.43            1.0             500                1000   \n",
       "3               0.72            1.0             500                1000   \n",
       "4               0.77            0.0             500                1000   \n",
       "\n",
       "    fund_manager risk_category sebi_category_code  \n",
       "0  Sohini Andani      Moderate               EC01  \n",
       "1  Sohini Andani      Moderate               EC01  \n",
       "2  R. Srinivasan     Very High               EC03  \n",
       "3  R. Srinivasan     Very High               EC03  \n",
       "4   Dinesh Ahuja           Low               DC02  "
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "c3e14779-4c38-4dab-b9b6-0b63d692b534",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(46000, 3)"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "e8c63751-3efc-48bd-9731-f991d95263d6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "amfi_code      int64\n",
       "date          object\n",
       "nav          float64\n",
       "dtype: object"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "9cffd207-46dc-44e7-9c52-5b5038e6da40",
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
       "      <th>amfi_code</th>\n",
       "      <th>date</th>\n",
       "      <th>nav</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>119551</td>\n",
       "      <td>2022-01-03</td>\n",
       "      <td>54.3856</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>119551</td>\n",
       "      <td>2022-01-04</td>\n",
       "      <td>54.3474</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>119551</td>\n",
       "      <td>2022-01-05</td>\n",
       "      <td>54.6869</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>119551</td>\n",
       "      <td>2022-01-06</td>\n",
       "      <td>55.4550</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>119551</td>\n",
       "      <td>2022-01-07</td>\n",
       "      <td>55.3692</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   amfi_code        date      nav\n",
       "0     119551  2022-01-03  54.3856\n",
       "1     119551  2022-01-04  54.3474\n",
       "2     119551  2022-01-05  54.6869\n",
       "3     119551  2022-01-06  55.4550\n",
       "4     119551  2022-01-07  55.3692"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "8c2856e0-d1bf-465c-9561-c07228f49517",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(90, 5)"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "8db270ac-ebc8-4589-b204-d4d9c13f2e06",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "date               object\n",
       "fund_house         object\n",
       "aum_lakh_crore    float64\n",
       "aum_crore           int64\n",
       "num_schemes         int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "87a4c1b1-b49c-450d-9f81-e2eb388c4d71",
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
       "      <th>date</th>\n",
       "      <th>fund_house</th>\n",
       "      <th>aum_lakh_crore</th>\n",
       "      <th>aum_crore</th>\n",
       "      <th>num_schemes</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2022-03-31</td>\n",
       "      <td>SBI Mutual Fund</td>\n",
       "      <td>6.05</td>\n",
       "      <td>605000</td>\n",
       "      <td>186</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2022-03-31</td>\n",
       "      <td>ICICI Prudential MF</td>\n",
       "      <td>4.65</td>\n",
       "      <td>465000</td>\n",
       "      <td>216</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2022-03-31</td>\n",
       "      <td>HDFC Mutual Fund</td>\n",
       "      <td>4.35</td>\n",
       "      <td>435000</td>\n",
       "      <td>195</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2022-03-31</td>\n",
       "      <td>Nippon India MF</td>\n",
       "      <td>2.70</td>\n",
       "      <td>270000</td>\n",
       "      <td>177</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2022-03-31</td>\n",
       "      <td>Kotak Mahindra MF</td>\n",
       "      <td>2.70</td>\n",
       "      <td>270000</td>\n",
       "      <td>168</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         date           fund_house  aum_lakh_crore  aum_crore  num_schemes\n",
       "0  2022-03-31      SBI Mutual Fund            6.05     605000          186\n",
       "1  2022-03-31  ICICI Prudential MF            4.65     465000          216\n",
       "2  2022-03-31     HDFC Mutual Fund            4.35     435000          195\n",
       "3  2022-03-31      Nippon India MF            2.70     270000          177\n",
       "4  2022-03-31    Kotak Mahindra MF            2.70     270000          168"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "3959e646-b454-4bf7-9d94-7b8511281196",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(48, 6)"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df3.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "327f5ef9-a505-467a-a25a-156316dafc81",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "month                         object\n",
       "sip_inflow_crore               int64\n",
       "active_sip_accounts_crore    float64\n",
       "new_sip_accounts_lakh        float64\n",
       "sip_aum_lakh_crore           float64\n",
       "yoy_growth_pct               float64\n",
       "dtype: object"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df3.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "426519ef-acd9-40d7-b53f-6933b1fcd9f4",
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
       "      <th>month</th>\n",
       "      <th>sip_inflow_crore</th>\n",
       "      <th>active_sip_accounts_crore</th>\n",
       "      <th>new_sip_accounts_lakh</th>\n",
       "      <th>sip_aum_lakh_crore</th>\n",
       "      <th>yoy_growth_pct</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2022-01</td>\n",
       "      <td>11517</td>\n",
       "      <td>4.91</td>\n",
       "      <td>9.10</td>\n",
       "      <td>4.80</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2022-02</td>\n",
       "      <td>11438</td>\n",
       "      <td>4.93</td>\n",
       "      <td>8.20</td>\n",
       "      <td>4.85</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2022-03</td>\n",
       "      <td>12328</td>\n",
       "      <td>5.09</td>\n",
       "      <td>10.50</td>\n",
       "      <td>5.01</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2022-04</td>\n",
       "      <td>11863</td>\n",
       "      <td>5.48</td>\n",
       "      <td>9.52</td>\n",
       "      <td>5.12</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2022-05</td>\n",
       "      <td>12286</td>\n",
       "      <td>5.55</td>\n",
       "      <td>8.10</td>\n",
       "      <td>5.15</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     month  sip_inflow_crore  active_sip_accounts_crore  \\\n",
       "0  2022-01             11517                       4.91   \n",
       "1  2022-02             11438                       4.93   \n",
       "2  2022-03             12328                       5.09   \n",
       "3  2022-04             11863                       5.48   \n",
       "4  2022-05             12286                       5.55   \n",
       "\n",
       "   new_sip_accounts_lakh  sip_aum_lakh_crore  yoy_growth_pct  \n",
       "0                   9.10                4.80             NaN  \n",
       "1                   8.20                4.85             NaN  \n",
       "2                  10.50                5.01             NaN  \n",
       "3                   9.52                5.12             NaN  \n",
       "4                   8.10                5.15             NaN  "
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df3.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "021dd361-a1d2-4dbe-87a3-2278bf114564",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(144, 3)"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df4.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "b8b34932-384a-4073-9272-33ec243420cd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "month                object\n",
       "category             object\n",
       "net_inflow_crore    float64\n",
       "dtype: object"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df4.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "17b62bd2-f8af-489d-8658-a1477e86e11f",
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
       "      <th>month</th>\n",
       "      <th>category</th>\n",
       "      <th>net_inflow_crore</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2024-04</td>\n",
       "      <td>Large Cap</td>\n",
       "      <td>2413.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2024-04</td>\n",
       "      <td>Mid Cap</td>\n",
       "      <td>3897.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2024-04</td>\n",
       "      <td>Small Cap</td>\n",
       "      <td>3533.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2024-04</td>\n",
       "      <td>Flexi Cap</td>\n",
       "      <td>4947.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2024-04</td>\n",
       "      <td>Large &amp; Mid Cap</td>\n",
       "      <td>4214.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     month         category  net_inflow_crore\n",
       "0  2024-04        Large Cap            2413.0\n",
       "1  2024-04          Mid Cap            3897.0\n",
       "2  2024-04        Small Cap            3533.0\n",
       "3  2024-04        Flexi Cap            4947.0\n",
       "4  2024-04  Large & Mid Cap            4214.0"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df4.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "0ae39abf-3ab5-4757-98c3-0e0c2ab1c1a9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(21, 6)"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df5.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "b1693c80-dc2d-440f-a0f1-102fff5ef680",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "month                   object\n",
       "total_folios_crore     float64\n",
       "equity_folios_crore    float64\n",
       "debt_folios_crore      float64\n",
       "hybrid_folios_crore    float64\n",
       "others_folios_crore    float64\n",
       "dtype: object"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df5.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "23218979-596b-4d32-9a24-cbc059d53699",
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
       "      <th>month</th>\n",
       "      <th>total_folios_crore</th>\n",
       "      <th>equity_folios_crore</th>\n",
       "      <th>debt_folios_crore</th>\n",
       "      <th>hybrid_folios_crore</th>\n",
       "      <th>others_folios_crore</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2022-01</td>\n",
       "      <td>13.26</td>\n",
       "      <td>9.28</td>\n",
       "      <td>1.86</td>\n",
       "      <td>0.80</td>\n",
       "      <td>1.33</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2022-04</td>\n",
       "      <td>13.91</td>\n",
       "      <td>9.74</td>\n",
       "      <td>1.95</td>\n",
       "      <td>0.83</td>\n",
       "      <td>1.39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2022-07</td>\n",
       "      <td>13.85</td>\n",
       "      <td>9.69</td>\n",
       "      <td>1.94</td>\n",
       "      <td>0.83</td>\n",
       "      <td>1.38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2022-10</td>\n",
       "      <td>14.12</td>\n",
       "      <td>9.88</td>\n",
       "      <td>1.98</td>\n",
       "      <td>0.85</td>\n",
       "      <td>1.41</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2023-01</td>\n",
       "      <td>14.81</td>\n",
       "      <td>10.37</td>\n",
       "      <td>2.07</td>\n",
       "      <td>0.89</td>\n",
       "      <td>1.48</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     month  total_folios_crore  equity_folios_crore  debt_folios_crore  \\\n",
       "0  2022-01               13.26                 9.28               1.86   \n",
       "1  2022-04               13.91                 9.74               1.95   \n",
       "2  2022-07               13.85                 9.69               1.94   \n",
       "3  2022-10               14.12                 9.88               1.98   \n",
       "4  2023-01               14.81                10.37               2.07   \n",
       "\n",
       "   hybrid_folios_crore  others_folios_crore  \n",
       "0                 0.80                 1.33  \n",
       "1                 0.83                 1.39  \n",
       "2                 0.83                 1.38  \n",
       "3                 0.85                 1.41  \n",
       "4                 0.89                 1.48  "
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df5.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "2bab79fa-8fe3-40c9-b2e7-25ba75e16aa7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(40, 19)"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df6.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "0441e0a9-a190-4404-af49-de19e33b2a11",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "amfi_code               int64\n",
       "scheme_name            object\n",
       "fund_house             object\n",
       "category               object\n",
       "plan                   object\n",
       "return_1yr_pct        float64\n",
       "return_3yr_pct        float64\n",
       "return_5yr_pct        float64\n",
       "benchmark_3yr_pct     float64\n",
       "alpha                 float64\n",
       "beta                  float64\n",
       "sharpe_ratio          float64\n",
       "sortino_ratio         float64\n",
       "std_dev_ann_pct       float64\n",
       "max_drawdown_pct      float64\n",
       "aum_crore               int64\n",
       "expense_ratio_pct     float64\n",
       "morningstar_rating      int64\n",
       "risk_grade             object\n",
       "dtype: object"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df6.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "72755aed-0d33-40b0-ab93-99a7a5b6f2bf",
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
       "      <th>amfi_code</th>\n",
       "      <th>scheme_name</th>\n",
       "      <th>fund_house</th>\n",
       "      <th>category</th>\n",
       "      <th>plan</th>\n",
       "      <th>return_1yr_pct</th>\n",
       "      <th>return_3yr_pct</th>\n",
       "      <th>return_5yr_pct</th>\n",
       "      <th>benchmark_3yr_pct</th>\n",
       "      <th>alpha</th>\n",
       "      <th>beta</th>\n",
       "      <th>sharpe_ratio</th>\n",
       "      <th>sortino_ratio</th>\n",
       "      <th>std_dev_ann_pct</th>\n",
       "      <th>max_drawdown_pct</th>\n",
       "      <th>aum_crore</th>\n",
       "      <th>expense_ratio_pct</th>\n",
       "      <th>morningstar_rating</th>\n",
       "      <th>risk_grade</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>119551</td>\n",
       "      <td>SBI Bluechip Fund - Regular Plan - Growth</td>\n",
       "      <td>SBI Mutual Fund</td>\n",
       "      <td>Large Cap</td>\n",
       "      <td>Regular</td>\n",
       "      <td>12.42</td>\n",
       "      <td>12.36</td>\n",
       "      <td>14.45</td>\n",
       "      <td>11.49</td>\n",
       "      <td>0.87</td>\n",
       "      <td>0.89</td>\n",
       "      <td>0.88</td>\n",
       "      <td>1.29</td>\n",
       "      <td>14.0</td>\n",
       "      <td>-21.70</td>\n",
       "      <td>14288</td>\n",
       "      <td>1.54</td>\n",
       "      <td>4</td>\n",
       "      <td>Moderate</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>119552</td>\n",
       "      <td>SBI Bluechip Fund - Direct Plan - Growth</td>\n",
       "      <td>SBI Mutual Fund</td>\n",
       "      <td>Large Cap</td>\n",
       "      <td>Direct</td>\n",
       "      <td>15.25</td>\n",
       "      <td>11.30</td>\n",
       "      <td>14.23</td>\n",
       "      <td>9.52</td>\n",
       "      <td>1.78</td>\n",
       "      <td>0.87</td>\n",
       "      <td>0.81</td>\n",
       "      <td>1.29</td>\n",
       "      <td>14.0</td>\n",
       "      <td>-24.43</td>\n",
       "      <td>1231</td>\n",
       "      <td>0.66</td>\n",
       "      <td>3</td>\n",
       "      <td>Moderate</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>119598</td>\n",
       "      <td>SBI Small Cap Fund - Regular Plan - Growth</td>\n",
       "      <td>SBI Mutual Fund</td>\n",
       "      <td>Small Cap</td>\n",
       "      <td>Regular</td>\n",
       "      <td>24.56</td>\n",
       "      <td>23.39</td>\n",
       "      <td>20.67</td>\n",
       "      <td>22.16</td>\n",
       "      <td>1.23</td>\n",
       "      <td>0.89</td>\n",
       "      <td>0.94</td>\n",
       "      <td>1.35</td>\n",
       "      <td>25.0</td>\n",
       "      <td>-13.35</td>\n",
       "      <td>19259</td>\n",
       "      <td>1.43</td>\n",
       "      <td>5</td>\n",
       "      <td>Very High</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>119599</td>\n",
       "      <td>SBI Small Cap Fund - Direct Plan - Growth</td>\n",
       "      <td>SBI Mutual Fund</td>\n",
       "      <td>Small Cap</td>\n",
       "      <td>Direct</td>\n",
       "      <td>20.59</td>\n",
       "      <td>23.14</td>\n",
       "      <td>21.82</td>\n",
       "      <td>22.01</td>\n",
       "      <td>1.13</td>\n",
       "      <td>1.04</td>\n",
       "      <td>0.93</td>\n",
       "      <td>1.67</td>\n",
       "      <td>25.0</td>\n",
       "      <td>-24.78</td>\n",
       "      <td>36061</td>\n",
       "      <td>0.72</td>\n",
       "      <td>4</td>\n",
       "      <td>Very High</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>119120</td>\n",
       "      <td>SBI Magnum Gilt Fund - Regular Plan - Growth</td>\n",
       "      <td>SBI Mutual Fund</td>\n",
       "      <td>Gilt</td>\n",
       "      <td>Regular</td>\n",
       "      <td>5.34</td>\n",
       "      <td>6.07</td>\n",
       "      <td>5.43</td>\n",
       "      <td>4.47</td>\n",
       "      <td>1.60</td>\n",
       "      <td>0.22</td>\n",
       "      <td>1.52</td>\n",
       "      <td>2.11</td>\n",
       "      <td>4.0</td>\n",
       "      <td>-2.30</td>\n",
       "      <td>24101</td>\n",
       "      <td>0.77</td>\n",
       "      <td>5</td>\n",
       "      <td>Low</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   amfi_code                                   scheme_name       fund_house  \\\n",
       "0     119551     SBI Bluechip Fund - Regular Plan - Growth  SBI Mutual Fund   \n",
       "1     119552      SBI Bluechip Fund - Direct Plan - Growth  SBI Mutual Fund   \n",
       "2     119598    SBI Small Cap Fund - Regular Plan - Growth  SBI Mutual Fund   \n",
       "3     119599     SBI Small Cap Fund - Direct Plan - Growth  SBI Mutual Fund   \n",
       "4     119120  SBI Magnum Gilt Fund - Regular Plan - Growth  SBI Mutual Fund   \n",
       "\n",
       "    category     plan  return_1yr_pct  return_3yr_pct  return_5yr_pct  \\\n",
       "0  Large Cap  Regular           12.42           12.36           14.45   \n",
       "1  Large Cap   Direct           15.25           11.30           14.23   \n",
       "2  Small Cap  Regular           24.56           23.39           20.67   \n",
       "3  Small Cap   Direct           20.59           23.14           21.82   \n",
       "4       Gilt  Regular            5.34            6.07            5.43   \n",
       "\n",
       "   benchmark_3yr_pct  alpha  beta  sharpe_ratio  sortino_ratio  \\\n",
       "0              11.49   0.87  0.89          0.88           1.29   \n",
       "1               9.52   1.78  0.87          0.81           1.29   \n",
       "2              22.16   1.23  0.89          0.94           1.35   \n",
       "3              22.01   1.13  1.04          0.93           1.67   \n",
       "4               4.47   1.60  0.22          1.52           2.11   \n",
       "\n",
       "   std_dev_ann_pct  max_drawdown_pct  aum_crore  expense_ratio_pct  \\\n",
       "0             14.0            -21.70      14288               1.54   \n",
       "1             14.0            -24.43       1231               0.66   \n",
       "2             25.0            -13.35      19259               1.43   \n",
       "3             25.0            -24.78      36061               0.72   \n",
       "4              4.0             -2.30      24101               0.77   \n",
       "\n",
       "   morningstar_rating risk_grade  \n",
       "0                   4   Moderate  \n",
       "1                   3   Moderate  \n",
       "2                   5  Very High  \n",
       "3                   4  Very High  \n",
       "4                   5        Low  "
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df6.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "3dd62b8e-ca36-4a14-8bce-0d54a263d078",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(32778, 13)"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df7.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "3fdeb312-f0a6-4405-870c-db7b4aa3fd71",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "investor_id            object\n",
       "transaction_date       object\n",
       "amfi_code               int64\n",
       "transaction_type       object\n",
       "amount_inr              int64\n",
       "state                  object\n",
       "city                   object\n",
       "city_tier              object\n",
       "age_group              object\n",
       "gender                 object\n",
       "annual_income_lakh    float64\n",
       "payment_mode           object\n",
       "kyc_status             object\n",
       "dtype: object"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df7.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "42d6f953-2d55-4e15-b7f4-55b663192dcd",
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
       "      <th>investor_id</th>\n",
       "      <th>transaction_date</th>\n",
       "      <th>amfi_code</th>\n",
       "      <th>transaction_type</th>\n",
       "      <th>amount_inr</th>\n",
       "      <th>state</th>\n",
       "      <th>city</th>\n",
       "      <th>city_tier</th>\n",
       "      <th>age_group</th>\n",
       "      <th>gender</th>\n",
       "      <th>annual_income_lakh</th>\n",
       "      <th>payment_mode</th>\n",
       "      <th>kyc_status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>INV003054</td>\n",
       "      <td>2024-01-01</td>\n",
       "      <td>119092</td>\n",
       "      <td>SIP</td>\n",
       "      <td>1834</td>\n",
       "      <td>Telangana</td>\n",
       "      <td>Hyderabad</td>\n",
       "      <td>T30</td>\n",
       "      <td>56+</td>\n",
       "      <td>Female</td>\n",
       "      <td>77.1</td>\n",
       "      <td>UPI</td>\n",
       "      <td>Verified</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>INV002952</td>\n",
       "      <td>2024-01-01</td>\n",
       "      <td>148567</td>\n",
       "      <td>Redemption</td>\n",
       "      <td>392882</td>\n",
       "      <td>Punjab</td>\n",
       "      <td>Amritsar</td>\n",
       "      <td>B30</td>\n",
       "      <td>18-25</td>\n",
       "      <td>Male</td>\n",
       "      <td>7.1</td>\n",
       "      <td>Cheque</td>\n",
       "      <td>Verified</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>INV003420</td>\n",
       "      <td>2024-01-01</td>\n",
       "      <td>118636</td>\n",
       "      <td>SIP</td>\n",
       "      <td>912</td>\n",
       "      <td>Haryana</td>\n",
       "      <td>Faridabad</td>\n",
       "      <td>B30</td>\n",
       "      <td>36-45</td>\n",
       "      <td>Male</td>\n",
       "      <td>47.2</td>\n",
       "      <td>Mandate</td>\n",
       "      <td>Verified</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>INV003436</td>\n",
       "      <td>2024-01-01</td>\n",
       "      <td>118634</td>\n",
       "      <td>SIP</td>\n",
       "      <td>1102</td>\n",
       "      <td>Maharashtra</td>\n",
       "      <td>Mumbai</td>\n",
       "      <td>T30</td>\n",
       "      <td>36-45</td>\n",
       "      <td>Female</td>\n",
       "      <td>54.4</td>\n",
       "      <td>Cheque</td>\n",
       "      <td>Pending</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>INV004691</td>\n",
       "      <td>2024-01-01</td>\n",
       "      <td>119094</td>\n",
       "      <td>Lumpsum</td>\n",
       "      <td>8682</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Noida</td>\n",
       "      <td>T30</td>\n",
       "      <td>26-35</td>\n",
       "      <td>Male</td>\n",
       "      <td>14.5</td>\n",
       "      <td>Net Banking</td>\n",
       "      <td>Pending</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  investor_id transaction_date  amfi_code transaction_type  amount_inr  \\\n",
       "0   INV003054       2024-01-01     119092              SIP        1834   \n",
       "1   INV002952       2024-01-01     148567       Redemption      392882   \n",
       "2   INV003420       2024-01-01     118636              SIP         912   \n",
       "3   INV003436       2024-01-01     118634              SIP        1102   \n",
       "4   INV004691       2024-01-01     119094          Lumpsum        8682   \n",
       "\n",
       "         state       city city_tier age_group  gender  annual_income_lakh  \\\n",
       "0    Telangana  Hyderabad       T30       56+  Female                77.1   \n",
       "1       Punjab   Amritsar       B30     18-25    Male                 7.1   \n",
       "2      Haryana  Faridabad       B30     36-45    Male                47.2   \n",
       "3  Maharashtra     Mumbai       T30     36-45  Female                54.4   \n",
       "4        Delhi      Noida       T30     26-35    Male                14.5   \n",
       "\n",
       "  payment_mode kyc_status  \n",
       "0          UPI   Verified  \n",
       "1       Cheque   Verified  \n",
       "2      Mandate   Verified  \n",
       "3       Cheque    Pending  \n",
       "4  Net Banking    Pending  "
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df7.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "d26f0800-f293-445b-b061-338ec9ae2970",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(322, 8)"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df8.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "3c2b60e6-9c1b-4c82-a52a-a1f6690b57e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "amfi_code              int64\n",
       "stock_symbol          object\n",
       "stock_name            object\n",
       "sector                object\n",
       "weight_pct           float64\n",
       "market_value_cr      float64\n",
       "current_price_inr    float64\n",
       "portfolio_date        object\n",
       "dtype: object"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df8.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "7f5febd2-c3f9-482c-8e6c-1081171d415a",
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
       "      <th>amfi_code</th>\n",
       "      <th>stock_symbol</th>\n",
       "      <th>stock_name</th>\n",
       "      <th>sector</th>\n",
       "      <th>weight_pct</th>\n",
       "      <th>market_value_cr</th>\n",
       "      <th>current_price_inr</th>\n",
       "      <th>portfolio_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>119551</td>\n",
       "      <td>POWERGRID</td>\n",
       "      <td>Power Grid Corporation</td>\n",
       "      <td>Utilities</td>\n",
       "      <td>13.85</td>\n",
       "      <td>737.09</td>\n",
       "      <td>6011.08</td>\n",
       "      <td>2025-12-31</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>119551</td>\n",
       "      <td>HDFCBANK</td>\n",
       "      <td>HDFC Bank Ltd</td>\n",
       "      <td>Banking</td>\n",
       "      <td>11.19</td>\n",
       "      <td>88.97</td>\n",
       "      <td>1074.65</td>\n",
       "      <td>2025-12-31</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>119551</td>\n",
       "      <td>GRASIM</td>\n",
       "      <td>Grasim Industries Ltd</td>\n",
       "      <td>Diversified</td>\n",
       "      <td>9.90</td>\n",
       "      <td>208.45</td>\n",
       "      <td>5964.59</td>\n",
       "      <td>2025-12-31</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>119551</td>\n",
       "      <td>DRREDDY</td>\n",
       "      <td>Dr. Reddy's Laboratories</td>\n",
       "      <td>Pharma</td>\n",
       "      <td>4.76</td>\n",
       "      <td>161.32</td>\n",
       "      <td>3748.82</td>\n",
       "      <td>2025-12-31</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>119551</td>\n",
       "      <td>ASIANPAINT</td>\n",
       "      <td>Asian Paints Ltd</td>\n",
       "      <td>Paints</td>\n",
       "      <td>10.25</td>\n",
       "      <td>725.90</td>\n",
       "      <td>1321.45</td>\n",
       "      <td>2025-12-31</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   amfi_code stock_symbol                stock_name       sector  weight_pct  \\\n",
       "0     119551    POWERGRID    Power Grid Corporation    Utilities       13.85   \n",
       "1     119551     HDFCBANK             HDFC Bank Ltd      Banking       11.19   \n",
       "2     119551       GRASIM     Grasim Industries Ltd  Diversified        9.90   \n",
       "3     119551      DRREDDY  Dr. Reddy's Laboratories       Pharma        4.76   \n",
       "4     119551   ASIANPAINT          Asian Paints Ltd       Paints       10.25   \n",
       "\n",
       "   market_value_cr  current_price_inr portfolio_date  \n",
       "0           737.09            6011.08     2025-12-31  \n",
       "1            88.97            1074.65     2025-12-31  \n",
       "2           208.45            5964.59     2025-12-31  \n",
       "3           161.32            3748.82     2025-12-31  \n",
       "4           725.90            1321.45     2025-12-31  "
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df8.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "faaa8a16-b34b-4005-93b2-d7a74201f721",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(8050, 3)"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df9.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "86109423-e9c8-4a45-8156-a91fe8199c6f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "date            object\n",
       "index_name      object\n",
       "close_value    float64\n",
       "dtype: object"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df9.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "ef3cbd4f-b8c1-4290-a477-f58d5ace9130",
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
       "      <th>date</th>\n",
       "      <th>index_name</th>\n",
       "      <th>close_value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2022-01-03</td>\n",
       "      <td>NIFTY50</td>\n",
       "      <td>17492.79</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2022-01-04</td>\n",
       "      <td>NIFTY50</td>\n",
       "      <td>17689.64</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2022-01-05</td>\n",
       "      <td>NIFTY50</td>\n",
       "      <td>17835.05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2022-01-06</td>\n",
       "      <td>NIFTY50</td>\n",
       "      <td>17878.51</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2022-01-07</td>\n",
       "      <td>NIFTY50</td>\n",
       "      <td>17759.15</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         date index_name  close_value\n",
       "0  2022-01-03    NIFTY50     17492.79\n",
       "1  2022-01-04    NIFTY50     17689.64\n",
       "2  2022-01-05    NIFTY50     17835.05\n",
       "3  2022-01-06    NIFTY50     17878.51\n",
       "4  2022-01-07    NIFTY50     17759.15"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df9.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "be465b80-7591-4258-8461-f0c7fbb6ecd3",
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
   "version": "3.13.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
