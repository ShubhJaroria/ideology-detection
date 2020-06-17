# By-Statement-Extractor
An extractor used to crawl the by &amp; about statements of dominant entities in India

To run the script for 1 given entity, simple call

  ```python by_statement_extractor.py --name <name-of-entity>```

To run the script for multiple entities (with their aliases), specify the paths this way

```python by_statement_extractor.py --names_path <path> --folder <domain-name> --aliases_path <path> --start <start-index> --end <end-index>```

This will search for all entities from the ```start_ind``` of the file till the ```end_ind```

Use the ```-N``` flag to limit the search (in the database) to top-N entities.

Example Queries:

```python by_statement_extractor.py --names_path './Input/power_elites.txt' --folder power_elites --aliases_path './Input/power_elite_alias_file.txt' --start 10 --end 20 --N 40000```

```python by_statement_extractor.py --names_path './Input/digital_india_entity_names.txt' --folder digital_india --start 0 --end 20 --N 40000```


Make sure to run the Stanford Core NLP as follows

```cd stanford-corenlp-full-2018-10-05```

```java -mx6g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -timeout 50000```
