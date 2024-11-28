import streamlit as st 
import functions


todos = functions.get_todos()
def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todo(todos)

st.title("My Todo application")
st.subheader("This is my todo app")
st.write("In this app is created to improve the productivity of the user")

# st.checkbox("Buy the groceries")
# st.checkbox("Throw the trash")
# st.checkbox("Buy mangoes")



for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[todo]
        st.rerun()



a = st.text_input(label="",
                  placeholder="Enter a new todo ..", 
                  on_change=add_todo,
                  key="new_todo")

# print(a)
# print("hello")

st.session_state



#  this entrire scipt is run once again, when the user reloads the webpage

