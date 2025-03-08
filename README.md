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

#### Modifications done to the streamlit app (othello.py)
Nous avons ajoute un bouton dans l'interface qui charge les algorithmes definis dans ce projet, ce qui evite l'utilisation du formulaire et accelere le developement. Le bouton invoque `play()` qui charge automatiquement le contenu et ajoute des lignes additionnelles dans le try catch pour debugger (ajoute la source et la ligne ayant cree l'erreur).






## Tâche 1 : Minimax amélioré 
La fonction d'evaluation de base n'est plus seulement evaluee par `evaluate_board(game.board)` aux feuilles, mais aussi par `evaluate_move(move)` a chaque niveau de l'arborescence, et par `evaluate_nb_positions(new_board,player)`. Si la ponderation est gardee a 100% pour chaque portion de la fx d'evaluation, alors `evaluate_move` domine, suivi de `evaluate_nb_positions`. 


On a la possibilite d'appeler `evaluate_nb_positions` aux feuilles plutot qu'a chaque niveau, mais cela lui ferait perdre davatange d'importance.


`eval_score, _ = PONDERATION1*minimax2(new_board, depth - 1, False, -player) + PONDERATION2*evaluate_move(move) + PONDERATION3*evaluate_nb_positions`




## Tâche 2 : Alpha Beta

## Tâche 3 : Monte-Carlo