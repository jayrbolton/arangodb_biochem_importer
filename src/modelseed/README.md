Generating (Regenerating) reaction similary and gene model ArangoDB

(startng from https://kbase-jira.atlassian.net/browse/SCT-1375)

1) Collect reference reaction (reactions.tsv) and compound  (compounds.tsv) data from here:

https://github.com/kbaseapps/BiochemistryAPI/tree/master/data

2) copy compounds.tsv to new_compounds.tsv, edit new_compounds.tsv and
    add InCHI string for hydrogen

< cpd00067    h	     H+	 H	1	ModelSEED	InChI=1S/p+1	1	1	0	
  0	      -9.53  0	 						
---
> cpd00067	h	H+	H	1	ModelSEED		1	1	0		
0 -9.53		0							



3) if you don't have the RDKit python library, 

   3a) obtain python library RDKit via anaconda
     http://rdkit.org/docs/Install.html#cross-platform-under-anaconda-python-fastest-install

   3b) create anaconda environment and invoke it

     ~/anaconda2/bin/conda create -c rdkit -n my-rdkit-env rdkit
    <<<installs bucketloads of crap>>>

4) invoke RDkit anaconda environment
  (~/Downloads) bash 
    bash-3.2$ source ~/anaconda3/bin/activate my-rdkit-env
    (my-rdkit-env) bash-3.2$

5) create the reaction similarity matrix

     $ ./pass6.py  >p6_pairs.all
