# Python Memory Leak

* `objgraph` module is extremely helpful with this
    * [Overview](https://mg.pov.lt/objgraph/), [PyPI](https://pypi.org/project/objgraph/)
* Sample run using `pdb` based on [objgraph overview examples](https://mg.pov.lt/objgraph/):

        PYTHONPATH=. python -m pdb yourprog.py --arg=your-arg
        (Pdb) run
        (Pdb) continue
        (Pdb) ^c
        (Pdb) import objgraph, random
        (Pdb) objgraph.show_most_common_types(limit=10)
        (Pdb) objgraph.show_growth(limit=10)
        (Pdb) objgraph.show_chain(
                  objgraph.find_backref_chain(
                      random.choice(objgraph.by_type("dict")),
                      objgraph.is_proper_module
                  ),
                  filename="chain.png"
              )
* [dozer](https://github.com/mgedmin/dozer) is also really helpful. It launches a webserver and serves heap status in a GUI on port 8000
* [This](https://stackoverflow.com/a/61260839/2833126) SO post goes through an excellent sample session using dozer and objgraph
* Sample Dozer startup from the [SO post](https://stackoverflow.com/a/61260839/2833126):

        import wsgiref.simple_server
        
        import dozer
        
        def run_dozer():
            app = dozer.Dozer(app=None, path="/")
            with wsgiref.simple_server.make_server("", 8000, app) as httpd:
                print("Serving Dozer on port 8000...")
                httpd.serve_forever()
        
        threading.Thread(target=run_dozer, daemon=True).start()
