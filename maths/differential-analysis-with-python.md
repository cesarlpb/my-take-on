# Differential Expression Analysis with Python

This curriculum adapts a traditional introduction to **differential expression analysis** (originally using R and Bioconductor) into a Python-based workflow.  
We will rely on `pandas`, `numpy`, `statsmodels`, `scikit-learn`, and `scanpy` for handling expression data, modeling, and visualization.

---

## 1. Differential Expression Analysis

To begin, you'll review the goals of differential expression analysis, manage gene expression data in Python, and run your first analysis.

- Differential expression analysis  
- Applications of differential expression analysis  
- Differential expression data  
- Create a boxplot  
- Expression data structures (`AnnData`, `DataFrame`)  
- Create an expression dataset object  
- Create a boxplot with an expression dataset  
- Specifying a linear model to compare 2 groups  
- Testing for differential expression between 2 groups  

---

## 2. Flexible Models for Common Study Designs

In this chapter, you'll learn how to construct linear models to test for differential expression for common experimental designs.

- Flexible linear models  
- Design matrix for group-means model  
- Contrasts matrix for group-means  
- Test for differential expression for group-means  
- Studies with more than two groups  
- Design matrix for 3 groups  
- Contrasts matrix for 3 groups  
- Test for differential expression for 3 groups  
- Factorial experimental design  
- Design matrix for 2x2 factorial  
- Contrasts matrix for 2x2 factorial  
- Test for differential expression for 2x2 factorial  

---

## 3. Pre- and Post-processing

Now that you've learned how to perform differential expression tests, next you'll learn how to normalize and filter feature data, check for technical batch effects, and assess the results.

- Normalizing and filtering  
- Normalize expression data  
- Filter genes  
- Accounting for technical batch effects  
- Visualize batch effects  
- Remove batch effects  
- Visualizing the results  
- Histogram of p-values  
- Volcano plot  
- Enrichment testing  
- KEGG pathway analysis  
- Gene ontology categories  

---

## 4. Case Study: Effect of Doxorubicin Treatment

In this final chapter, you'll perform an end-to-end differential expression analysis of a study that uses a factorial design to assess the impact of the cancer drug **doxorubicin** on the hearts of mice with different genetic backgrounds.

- Pre-process the data  
- Pre-process features  
- Boxplot of Top2b  
- Check sources of variation  
- Model the data  
- Design matrix  
- Contrasts matrix  
- Test for differential expression  
- Inspect the results  
- Histogram of p-values  
- Volcano plot  
- Pathway enrichment  
- Conclusion  

---
