#i will import the the printing  function from the functions.extend module 
from funcrions_extend import print_models as pm 
from funcrions_extend import show_completed_model as sm

#now the function print_models is now pm 
unprinted_designs= ['red','blue','car']
completed_model= []

pm('unprinted_designs','completed_models')
sm('completed_models')