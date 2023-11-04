# aanmaken bestand
from pickle import dump

kaaswinkel = [ ("Roquefort", 12, 15.23), 
    ("White Stilton", 25, 19.02), ("Cheddar", 5, 0.67) ]

# open file for writing in binary mode
fp = open( "pc_cheese.pck", "wb" )
# pickle in actie
dump( kaaswinkel, fp )
fp.close()

print( "uitvoer gereed" )

#uitlezen bestand
from pickle import load

fp = open( "pc_cheese.pck", "rb" )
buffer = load( fp )
fp.close()

print( type( buffer ) )
print( buffer )