This project hosts an AI competition for Othello, where users can submit their custom AI strategies to compete against a Minimax-based AI. The app is built using Streamlit.


🔗 Live App: [Othello AI Competition](https://othelloift3335.streamlit.app/)



# README 

#### Collaborators
Emanuel Rollin 20106951
Anne Sohpie Rozefort 20189221

## Dependencies
How to install the dependencies from `requirement.txt` :

Create a virtual environment in your project directory:
```bash
python -m venv venv
.\venv\Scripts\activate
```

And then install them with :
```bash
pip install -r requirements.txt
```

Make sure the environment is selected. Use the shortcut `Ctrl+Shift+P` and pick the `Python: Select Interpreter` option and select the venv interpreter.



## Launching the streamlit app

In your VSCode CLI, in the project directory, enter the following command (the port can be changed to any port you want):
`streamlit run othello.py --server.port 8501`

Then, simply access `http://localhost:8501/` in your **browser** if it did not automatically open.

### Modifications done to the streamlit app (othello.py)
Nous avons ajoute un bouton dans l'interface qui charge les algorithmes definis dans ce projet, ce qui evite l'utilisation du formulaire et accelere le developement. Le bouton invoque `play()` qui charge automatiquement le contenu et ajoute des lignes additionnelles dans le try catch pour debugger (ajoute la source et la ligne ayant cree l'erreur).

Nous avons aussi reduit le sleep a 0.1s pour accelerer le jeu.




## Tâche 1 : Minimax amélioré 
La fonction d'evaluation de base n'est plus seulement evaluee par `evaluate_board(game.board)` aux feuilles, mais aussi par `evaluate_move(move)` a chaque niveau de l'arborescence, et par `evaluate_nb_positions(new_board,player)`. Si la ponderation est gardee a 100% pour chaque portion de la fx d'evaluation, alors `evaluate_move` domine, suivi de `evaluate_nb_positions`. 


On a la possibilite d'appeler `evaluate_nb_positions` aux feuilles plutot qu'a chaque niveau, mais cela lui ferait perdre davatange d'importance.


`eval_score, _ = PONDERATION1*minimax2(new_board, depth - 1, False, -player) + PONDERATION2*evaluate_move(move) + PONDERATION3*evaluate_nb_positions`


### Minimax VS Minimax

Avec une ponderation 1,0,0 on a l'equivalent d'un minimax versus minimax. Si on garde un depth de 3, noir est systematiquement en desavantage sur blanc et la partie se termine avec -40.

Si on garde la ponderation 1,0,0 mais qu'on augmente le nombre de pli / depth a 6, on remarque que le jeu est fortement ralenti, et que la performance demeure a -40, comme quoi le nombre de pli n'est pas le seul facteur contribuant. En observant un match, on remarque que l'avarice dicte le processus de decision, et que meme en ayant de l'avance, le minimax neglige les positions fortes et s'ecroule rapitement lorsque les coins sont conquis.

Avec depth a 5 et ponderation 1,1,1 : On a un score de 46 (reste 9 pieces blanches). Le jeu est legerement ralenti et cela affecte la qualite de vie de l'application.

Avec depth a 4 et ponderation 1,1,1 : On a un score de 32 (reste 16 pieces blanches). Le jeu ne semble pas ralenti et la performance diminue un peu.

Avec depth a 4 et ponderation 3,1,6 : On a un score de 42 (reste 11 pieces blanches). Changer ce ratio permet d'ameliorer certaines choses et d'amoindrir d'autres, il serait interessant de tester toutes les permutations et les stocker dans un log file (a faire si le temps le permet).

Constatations : 
- La valeur des coins est importante en debut de partie, mais importe peu en fin de partie. 
- L'automate peut se coincer en fin de partie s'il favorise des actions blocantes, alors l'heuristique `evaluate_nb_positions` gagne en importance vers la fin de la partie
- Les mouvements qui gagnent le plus de cases sont critiques pour maximiser une fin de partie.

Amelioration suggeree : changer la ponderation en fonction de la progression du jeu.

```python
#On peut resumer la logique ainsi meme si un peu plus detaillee en code:
gametime = 1
PONDERATION1 = 6 if gametime>10 else 3
PONDERATION2 = 0 if gametime>10 else 1
PONDERATION3 = 9 if gametime>10 else 6
```

Avec cette nouvelle ponderation dynamique, notre algorithme accepte de laisser tomber les positions fortes en fin de partie et se concentre sur l'attaque. Notre score augmente a 56 (reste 4 pieces blanches).

## Tâche 2 : Alpha Beta

## Tâche 3 : Monte-Carlo