import numpy as np
import random 
import string
import csv
from datetime import *
from sklearn.model_selection import KFold 


class toyData(object):
    """class which ingests the data for downstream use 

    Args:
        parameter (row): number of rows for generateToyData()
        parameter (col): number of columns for generateToyData()
        parameter(n_folds): number of folds for k-fold cross validator variable. Must be at least 2
    """
    
    def __init__(self, row, col, n_folds):
        self.row = row 
        self.col = col 
        self.n_folds = n_folds
        
    
    def generateToyData(self, preProcessing = bool):
        """Toy data for testing purposes only

        Returns:
            array: random data using row and col as user input
        """
        M = np.random.rand(self.row, self.col)
        L = np.random.rand(M.shape[0])
        L = np.rint(L)
        self.data = (M, L, self.n_folds)
        if preProcessing == True:
            """Preprocesses passed data if needed

            Returns:
                constant M: ndarray of dtype float64
                constant L: ndarray with shape of M[0]
                variable kf: K-Fold Cross Validator
            """
            data = toyData(self.row, self.col, self.n_folds).generateToyData()
            M, L, n_folds = data
            self.M = M 
            self.L = L 
            self.kf = KFold(n_splits = self.n_folds)
            return self.M, self.L, self.kf
        else:
            return self.data
    
    def generateToyFinancialData(self, preProcessing = bool, label = None):
        """Generates random financial order data. The purpose of this is to have reusable, non similar financial data
        for resusable testing that is as realistic to a raw dataset as possible.

        Args:
            preProcessing (bool, optional): alters data to be preprocessed. Defaults to bool.
            label (any, optional): _description_. Defaults to None.
        """
        self.data = {}
        for ids in range(self.row):
            self.data[ids] = {
                'InvoiceNo': np.random.randint(1000, 7000)
                , 'CustomerID': np.random.randint(0, 8000)
                , 'StockCodes': str(np.random.randint(1000, 3000)) + str(random.choice(string.ascii_letters).upper())
                , 'Quantity': np.random.randint(0, 100)
                , 'InvoiceDate': str(random.random() * (date(2000, 1, 1) - date.today()) + date.today())
                , 'UnitPriceUSD': np.random.randint(50, 5000)
                , 'Country': random.choice(['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe']
                                            )
            }
        header = sorted(set(i for b in map(dict.keys, self.data.values()) for i in b))
        dateTimeInsert = datetime.now()
        with open(f'data/csv/{dateTimeInsert}generated_retail_data.csv', 'w') as f:
            write = csv.writer(f)
            write.writerow(['IDs', *header])
            for a, b in self.data.items():
                write.writerow([a] + [b.get(i, '') for i in header])
        if preProcessing == True:
            """
            preProcessing assigns M, L, and KF for later use
            """
            self.M = {k: self.data[k] for k in set(list(self.data.keys())) - set(list(label))}
            self.L = {k: self.data[k] for k in set(list(label))}
            self.kf = KFold(n_splits = self.n_folds, random_state = 123, shuffle = True)
            return self.M, self.L, self.kf
        else: 
            return self.data
            
          
        