#!/usr/bin/env python
# coding: utf-8

# # POKEMON

# In[1]:


import pandas as pd
df = pd.read_csv("pokemons.csv")


# In[2]:


df


# # somma le statistiche dei pokemon

# In[ ]:


import pandas as pd

def add():
    df = pd.read_csv("pokemons.csv")

    
    def calculate_total(name):# crea un dataframe con un nome specifico
        pokemon = df[df['name'] == name]
        if len(pokemon) == 0:
            return "Pokemon non trovato"# e quando il pokemon non c'è nel df
        else:
            total_stats = pokemon[['hp', 'atk', 'def', 'spatk', 'spdef', 'speed']].sum(axis=1).values[0]
            return f"la somma delle statistiche di {name.capitalize()} è {total_stats}"

    pokemon_name = input("Inserisci il nome del Pokemon: ").lower()  # Test funzione
    print(calculate_total(pokemon_name))

add()



# # sottrae le statistiche dei pokemon

# In[ ]:


import pandas as pd

def sott():
    df = pd.read_csv("pokemons.csv")

    def calculate_difference(name):
        pokemon = df[df['name'] == name]
        if len(pokemon) == 0:
            return "Pokemon non trovato"
        else:
            total_stats = pokemon[['hp', 'atk', 'def', 'spatk', 'spdef', 'speed']].sum(axis=1).values[0]
            return f"La differenza delle statistiche di {name.capitalize()} è {-total_stats}" # Utilizzo di sottrazione

    pokemon_name = input("Inserisci il nome del Pokemon: ").lower()
    print(calculate_difference(pokemon_name))

sott()


# # moltiplica le statistiche dei pokemon

# In[1]:


import pandas as pd

def mol():
    df = pd.read_csv("pokemons.csv")

    def calculate_multiplication(name):
        pokemon = df[df['name'] == name]
        if len(pokemon) == 0:
            return "Pokemon non trovato"
        else:
            total_stats = pokemon[['hp', 'atk', 'def', 'spatk', 'spdef', 'speed']].prod(axis=1).values[0]
            return f"La moltiplicazione delle statistiche di {name.capitalize()} è {total_stats}"

    pokemon_name = input("Inserisci il nome del Pokemon: ").lower()
    print(calculate_multiplication(pokemon_name))

mol()


# # divide le statistiche dei pokemon

# In[2]:


import pandas as pd

def div():
    df = pd.read_csv("pokemons.csv")

    def calculate_division(name):
        pokemon = df[df['name'] == name]
        if len(pokemon) == 0:
            return "Pokemon non trovato"
        else:
            total_stats = pokemon[['hp', 'atk', 'def', 'spatk', 'spdef', 'speed']].mean(axis=1).values[0]
            return f"La divisione delle statistiche di {name.capitalize()} è {total_stats}"

    pokemon_name = input("Inserisci il nome del Pokemon: ").lower()
    print(calculate_division(pokemon_name))

div()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




