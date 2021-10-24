import wikipediaapi

def pesquisara(pesquisa):
		print("Pesquisa Wikipédia")
		wikipidia(f"{pesquisa}")


def wikipidia(pesquisa):
  wiki_wiki = wikipediaapi.Wikipedia('pt')
  page_py = wiki_wiki.page(pesquisa)
  titulu = page_py.title
  if page_py.exists() == True:
			print("Titulo: {}".format(titulu))
			print("Resumo: {}".format(page_py.summary[0:500]))