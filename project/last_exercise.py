
"""
ArgParse Assignment is written below. Test in command prompt by writing e.g.:
        
    python last_exercise.py -s 12345 -t 0.7 -m "x1, x2, x3" -p

with this code we retrieve the following:
    -s: sets random seed to 12345
    -t: sets train sample to 0.7 and test sample to 0.3                 
    -m: sets model to y ~ b0 + b1*x1 + b2*x2 + b3*x3                    
    -p: specifies to plot the model (exlcluding -p results in no plot)

run python last_exercise.py --help in the command prompt to retrieve description,
optional arguments, and epilog.

"""


# Import argparse
import argparse, textwrap

# Argparse arguments
parser = argparse.ArgumentParser(formatter_class = argparse.RawDescriptionHelpFormatter,
                                 description = textwrap.dedent('''\
                                                               -------------------------------------------------------------------------------------------------------------
                                                                               A tester program for different Logistic Regression Models.
                                                               -------------------------------------------------------------------------------------------------------------
                                                               This tester uses the LogisticRegression, diagnosticPlot, and the DataSet classes.
                                                               
                                                               It uses the DataSet class to correctly modify the data format, it then runs the logistic regressions
                                                               (using LogisticRegression) on the specified models using log optimization to fit the models, and 
                                                               finally it plots the ROC Curve using the diagnosticPlot class.
                                                               
                                                               The tester program runs a logistic regression on different 
                                                               models based on which covariates are specified:
                                                                   (1) "x1"         runs "y ~ b0 + b1*x1"
                                                                   (2) "x1, x2"     runs "y ~ b0 + b1*x1 +b2*x2"
                                                                   (3) "x1, x3"     runs "y ~ b0 + b1*x1 + b2*x3"
                                                                   (4) "x2, x3"     runs "y ~ b0 + b1*x2 + b2*x3"
                                                                   (5) "x1, x2, x3" runs "y ~ b0 + b1*x1 +b2*x2 + b3*x3"
                                                               
                                                               Outputs: i) model specifications, ii) fitted parameters, iii) model accuracy (ROC Score), iv) plots ROC Curve
                                                               
                                                               '''),
                                epilog = textwrap.dedent('''\
                                                               -------------------------------------------------------------------------------------------------------------
                                                               The DataSet class is constructed using an input. When running the code in the
                                                               command prompt it will ask: "Is the input data transposed?", here you shall write
                                                               "False" as the dataset we are using for this exercise is not transposed.                                                        
                                                             '''))


parser.add_argument("-s", "--seed",  default = 12345, type = int, metavar ="",  required=False, help="Seed to replicate results. Default value set to 12345")
parser.add_argument("-t", "--train", type = float, metavar ="",  required=True, help="Required Argument. Size of train set (e.g. 0.7 equals 0.7 into train set and 0.3 into test set)" )
parser.add_argument("-c", "--covars", metavar="", required = True, choices = ["x1", "x1, x2", "x1, x3", "x2, x3", "x1, x2, x3"] , help='Required Argument. You can choose between: (1) "x1", (2) "x1, x2", (3) "x1, x3", (4) "x2, x3", and (5) "x1, x2, x3" ')
parser.add_argument("-p", "--make_plot", action="store_true", help="Will not plot on default, specify -p to plot")
args = parser.parse_args()




"""
Below is the code from the midterm, adjusted for ArgParse arguments

"""

# Import classes and packages
from LinearModels import *
from diagnosticPlot import *
from DataSet import *
import numpy as np
import statsmodels.api as sm

# Load dataset spector
spector = sm.datasets.spector.load_pandas()

# Feed into DataSet class
data = DataSet(spector.exog.values, spector.endog.values, scaled=False)
data.add_constant()

# Test and train sets
data.train_test(train_set = args.train, seed = args.seed)
x_te = data.x_te
x_tr = data.x_tr
y_te = data.y_te
y_tr = data.y_tr

# Define model based on covariates chosen
if args.covars == "x1":
    model = "y ~ b0 + b1*x1"
if args.covars == "x1, x2":
    model = "y ~ b0 + b1*x1 + b2*x2"
if args.covars == "x1, x3":
    model = "y ~ b0 + b1*x1 + b2*x3"
if args.covars == "x2, x3":
    model = "y ~ b0 + b1*x2 + b2*x3"
if args.covars == "x1, x2, x3":
    model = "y ~ b0 + b1*x1 + b2*x2 + b3*x3"

# Define and fit model parameters
reg_1 = LogisticRegression(x_tr, y_tr)
reg_1.linearMethod(model) 
reg_1.optimize()

# Print LogitRegression summary
print(reg_1.summary())

# Plot Regression if specified as true with y test and predicted mu on test set depending on model
if args.make_plot == True:
    if model == "y ~ b0 + b1*x1":
        dp_1 = diagnosticPlot(reg_1)
        dp_1.plot(y_te, reg_1.predict(reg_1.params, x_te[(0,1),:]))    
    elif model == "y ~ b0 + b1*x1 + b2*x2":
        dp_1 = diagnosticPlot(reg_1)
        dp_1.plot(y_te, reg_1.predict(reg_1.params, x_te[(0,1,2),:]))    
    elif model == "y ~ b0 + b1*x1 + b2*x3":
        dp_1 = diagnosticPlot(reg_1)
        dp_1.plot(y_te, reg_1.predict(reg_1.params, x_te[(0,1,3),:]))    
    elif model == "y ~ b0 + b1*x2 + b2*x3":
        dp_1 = diagnosticPlot(reg_1)
        dp_1.plot(y_te, reg_1.predict(reg_1.params, x_te[(0,2,3),:]))    
    elif model == "y ~ b0 + b1*x1 + b2*x2 + b3*x3":
        dp_1 = diagnosticPlot(reg_1)
        dp_1.plot(y_te, reg_1.predict(reg_1.params, x_te))


