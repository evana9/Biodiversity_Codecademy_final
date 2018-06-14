import codecademylib
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import chi2_contingency

# Loading the Data
species = pd.read_csv('species_info.csv')

# print species.head()

# Inspecting the DataFrame
species_count = len(species)

species_type = species.category.unique()

conservation_statuses = species.conservation_status.unique()

# Analyze Species Conservation Status
conservation_counts = species.groupby('conservation_status').scientific_name.count().reset_index()

# print conservation_counts

# Analyze Species Conservation Status II
species.fillna('No Intervention', inplace = True)

conservation_counts_fixed = species.groupby('conservation_status').scientific_name.count().reset_index()

# Plotting Conservation Status by Species
protection_counts = species.groupby('conservation_status')\
    .scientific_name.count().reset_index()\
    .sort_values(by='scientific_name')
    
# plt.figure(figsize=(10, 4))
# ax = plt.subplot()
# plt.bar(range(len(protection_counts)),
#        protection_counts.scientific_name.values)
# ax.set_xticks(range(len(protection_counts)))
# ax.set_xticklabels(protection_counts.conservation_status.values)
# plt.ylabel('Number of Species')
# plt.title('Conservation Status by Species')
# labels = [e.get_text() for e in ax.get_xticklabels()]
# print ax.get_title()
# plt.show()

species['is_protected'] = species.conservation_status != 'No Intervention'

category_counts = species.groupby(['category', 'is_protected'])\
                         .scientific_name.count().reset_index()
  
# print category_counts.head()

category_pivot = category_counts.pivot(columns='is_protected', index='category', values='scientific_name').reset_index()

category_pivot.columns = ['category', 'not_protected', 'protected']

category_pivot['percent_protected'] = category_pivot.protected / (category_pivot.protected + category_pivot.not_protected)

print category_pivot.head()

plt.figure(figsize=(10,6))
plt.bar(range(len(category_pivot)), category_pivot.percent_protected)
ax = plt.subplot()
ax.set_xticks(range(len(category_pivot)))
ax.set_xticklabels(category_pivot.category, fontsize=10)
plt.ylabel('Percentage of protected species')
plt.title('Protected species, by category')
plt.show()

# Chi-square test
#        protected   not_protected  
# Mammal      30       146  
# Bird        75        413

contingency = [[30, 146],
              [75, 413]]

chi2, pval, dof, expected = chi2_contingency(contingency)

print pval   # not significant

#         protected   not_protected  
# Mammal      30       146  
# Reptile      5        73

contingency_reptile_mammal = [[5, 73], 
                             [30, 146]]

chi2, pval_reptile_mammal, dof, expected = chi2_contingency(contingency_reptile_mammal)

print pval_reptile_mammal   # significant

# Comparing amphibian_bird
contingency_amphibian_bird = [[7, 72], 
                             [75, 413]]

chi2, pval_amphibian_bird, dof, expected = chi2_contingency(contingency_amphibian_bird)

print pval_amphibian_bird  # not significant

# Comparing amphibian_mammal
contingency_amphibian_mammal = [[7, 72], 
                               [30, 146]]

chi2, pval_amphibian_mammal, dof, expected = chi2_contingency(contingency_amphibian_mammal)

print pval_amphibian_mammal  # not significant

# Comparing fish_bird
contingency_fish_bird = [[11, 115],
                        [75, 413]]
chi2, pval_fish_bird, dof, expected = chi2_contingency(contingency_fish_bird)

print pval_fish_bird    # not significant

# Comparing non_vascular_plant_bird
contingency_non_vascular_plant_bird = [[5, 328], [75, 413]]

chi2, pval_non_vascular_plant_bird, dof, expected = chi2_contingency(contingency_non_vascular_plant_bird)

print pval_non_vascular_plant_bird   # significant

# Comparing vascular_plant_bird
contingency_vascular_plant_bird = [[46, 4216], [75, 413]]

chi2, pval_vascular_plant_bird, dof, expected = chi2_contingency(contingency_vascular_plant_bird)

print pval_vascular_plant_bird   # significant

#Comparing fish_amphibian
contingency_fish_amphibian = [[11, 115], [7, 73]]

chi2, pval_fish_amphibian, dof, expected = chi2_contingency(contingency_fish_amphibian)

print pval_fish_amphibian   # not significant

# Comparing reptile_fish
contingency_reptile_fish = [[5, 73],
                           [11, 115]]

chi2, pval_reptile_fish, dof, expected = chi2_contingency(contingency_reptile_fish)

print pval_reptile_fish   # not significant

# Comparing reptile_bird
contingency_reptile_bird = [[5, 73], 
                          [75, 413]]

chi2, pval_reptile_bird, dof, expected = chi2_contingency(contingency_reptile_bird)

print pval_reptile_bird   # not significant, on the border of being significant

# Comparing fish_mammal
contingency_fish_mammal = [[11, 115],
                          [30, 146]]

chi2, pval_fish_mammal, dof, expected = chi2_contingency(contingency_fish_mammal)

print pval_fish_mammal   # not significant, on the border of being significant

# Comparing reptile_vascular_plants
contingency_reptile_vascular_plants = [[5, 73], [46, 4216]]

chi2, pval_reptile_vascular_plants, dof, expected = chi2_contingency(contingency_reptile_vascular_plants)

print pval_reptile_vascular_plants  # significant

# Comparing mammal_non_vascular_plant
contingency_mammal_non_vascular_plant = [[30, 146], [5, 328]]

chi2, pval_mammal_non_vascular_plant, dof, expected = chi2_contingency(contingency_mammal_non_vascular_plant)

print pval_mammal_non_vascular_plant # significant 

# Comparing vascular_plants_non_vascular_plants
contingency_vascular_plants_non_vascular_plants = [[46, 4216], [5, 328]]

chi2, pval_vascular_plants_non_vascular_plants, dof, expected = chi2_contingency(contingency_vascular_plants_non_vascular_plants)

print pval_vascular_plants_non_vascular_plants   # not significant

# Comparing reptile_non_vascular_plant
contingency_reptile_non_vascular_plant = [[5, 73], [5, 328]]

chi2, pval_reptile_non_vascular_plant, dof, expected = chi2_contingency(contingency_reptile_non_vascular_plant)

print pval_reptile_non_vascular_plant   # significant