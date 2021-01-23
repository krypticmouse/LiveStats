import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.api import qqplot_2samples
sns.set_style('darkgrid')

class CLT:
    def __init__(self, element_count = 30, sample_size = 100):
        self.element_count = element_count
        self.sample_size = sample_size
        self.normal_dist = np.random.standard_normal(10000)
        self.avl_dist = {
            'normal': self.normal_dist,
            'uniform': np.random.uniform(-10, 10, 10000),
            't': np.random.standard_t(1000, size = 10000),
            'gamma': np.random.standard_gamma(0.5, size = 10000),
            'exponential': np.random.standard_exponential(size = 10000)
        }
    
    def get_random_indices(self):
        return np.random.choice(self.data.shape[0], 
                                self.element_count, 
                                replace=True) 
    
    def generate_mean_distribution(self, data = 'normal'):
        if str(type(data)) != "<class 'str'>":
            self.data = np.array(data)
            
        else:
            if data in self.avl_dist.keys():
                self.data = self.avl_dist[data]
            else:
                raise Exception(f'Distribution available are {tuple(self.avl_dist.keys())}')
        
        l = []
        for _ in range(self.sample_size):
            sample = self.data.copy()
            np.random.shuffle(sample)
            l.append(sample[:self.sample_size].mean())
        return l
    
    def run(self, data = 'normal'):
        mean_dist = self.generate_mean_distribution(data)
        mean_of_sample = np.mean(mean_dist)
        sd_of_sample = np.std(mean_dist)
        
        print(f'Mean of Mean Distribution: {mean_of_sample}')
        print(f'Mean of Data Distribution: {np.mean(self.data)}')
        print(f'S.D. of Mean Distribution: {sd_of_sample}')
        print(f'S.D. of Data Distribution: {np.std(self.data)}')
        cust_norm = np.random.normal(mean_of_sample, sd_of_sample, self.sample_size)
        
        plt.figure(figsize = (14,10))
        ax1 = plt.subplot2grid ((2, 2), (0, 0)) 
        ax1 = sns.distplot(cust_norm)
        ax1 = plt.title('Normal Distribution')
        
        ax2 = plt.subplot2grid ((2, 2), (0, 1)) 
        ax2 = sns.distplot(mean_dist)
        ax2 = plt.title('Mean Distribution')
        
        ax3 = plt.subplot2grid ((2, 2), (1, 0), colspan=2) 
        ax3 = sns.distplot(self.data)
        ax3 = plt.title('Data Distribution')
        
        qqplot_2samples(np.array(mean_dist),cust_norm, line = '45')
        
        plt.show()