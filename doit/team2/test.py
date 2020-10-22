import sys
import cardGame.GameSound.gameEcho

print(cardGame.GameSound.gameEcho.echo_test())
print(sys.path)

#%%
sys.path.remove("C:\\Users\\BCBL\\Documents\\doit")
print(sys.path)

#%%
import cardGame.GameSound.gameEcho
print(cardGame.GameSound.gameEcho.echo_test())

#%%
sys.path.append("C:/Users/BCBL/Documents/doit")
print(sys.path)

#%%
import cardGame.GameSound.gameEcho
print(cardGame.GameSound.gameEcho.echo_test())