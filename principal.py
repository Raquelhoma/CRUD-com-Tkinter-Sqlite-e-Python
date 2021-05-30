from tkinter import *

def cadAlunos():
    import cadastrarAlunos
def cadMat():
    import cadastrarMatricula
def cadTurma():
    import cadastrarTurma
def atualizarAluno():
    import atualizarAluno
def atualizarMat():
    import atualizarMatricula
def atualizarTurma():
    import atualizarTurma
def listarAlunos():
    import listarAlunos
def listarMat():
    import listarMatriculas
def listarTurmas():
    import listarTurmas
def deletarAlunos():
    import deletarAluno
def deletarMat():
    import deletarMatricula
def deletarTurma():
    import deletarTurma

menuprincipal = Tk()
menuprincipal.title('Escolha uma opcão - Universidade da Felicidade')


botao = Button(menuprincipal, text='Cadastrar Novo Aluno',width='22', height='2', command=cadAlunos)
botao.grid(row=0, column=0)

botao2 = Button(menuprincipal, text='Atualizar Cadastro Aluno',width='22', height='2', command=atualizarAluno)
botao2.grid(row=2, column=0)

botao3 = Button(menuprincipal, text='Listar Alunos Cadastrados',width='22', height='2', command=listarAlunos)
botao3.grid(row=4, column=0)

botao4 = Button(menuprincipal, text='Cadastrar Nova Turma',width='22', height='2', command=cadTurma)
botao4.grid(row=0, column=1)

botao5 = Button(menuprincipal, text='Atualizar Cadastro Turma',width='22', height='2', command=atualizarTurma)
botao5.grid(row=2, column=1)

botao6 = Button(menuprincipal, text='Listar Turmas Cadastrados',width='22', height='2', command=listarTurmas)
botao6.grid(row=4, column=1)

botao7 = Button(menuprincipal, text='Cadastrar Nova Matrícula',width='22', height='2', command=cadMat)
botao7.grid(row=0, column=2)

botao8 = Button(menuprincipal, text='Atualizar Matrícula',width='22', height='2', command=atualizarMat)
botao8.grid(row=2, column=2)

botao9 = Button(menuprincipal, text='Listar Matrículas',width='22', height='2', command=listarMat)
botao9.grid(row=4, column=2)

botao10 = Button(menuprincipal, text='Deletar Aluno',width='22', height='2', command=deletarAlunos)
botao10.grid(row=0, column=3)

botao11 = Button(menuprincipal, text='Deletar Turma',width='22', height='2', command=deletarTurma)
botao11.grid(row=2, column=3)

botao12 = Button(menuprincipal, text='Deletar Matrícula',width='22', height='2', command=deletarMat)
botao12.grid(row=4, column=3)

botao_fechar = Button(menuprincipal, text='Fechar', width='22', height='2', command= menuprincipal.destroy)
botao_fechar.grid(row=5, column=3)

menuprincipal.mainloop()







