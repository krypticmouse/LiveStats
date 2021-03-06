import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
sns.set_style('darkgrid')

class LLN:
    def __init__(self):
        self.normal_dist = np.random.standard_normal(10000)
        self.avl_dist = {
            'normal': self.normal_dist,
            'uniform': np.random.uniform(-10, 10, 10000),
            't': np.random.standard_t(1000, size = 10000),
            'gamma': np.random.standard_gamma(0.5, size = 10000),
            'exponential': np.random.standard_exponential(size = 10000)
        }
    
    def generate_sample_distribution(self, data = 'normal'):
        if str(type(data)) != "<class 'str'>":
            self.data = np.array(data)
            
        else:
            if data in self.avl_dist.keys():
                self.data = self.avl_dist[data]
            else:
                raise Exception(f'Distribution available are {tuple(self.avl_dist.keys())}')
        
        if self.sample_size is None or self.sample_size > len(self.data):
            warnings.warn('Sample Size exceeds Population Size changing it to 50%')
            self.sample_size = int(0.5 * len(self.data))

        sample = self.data.copy()
        np.random.shuffle(sample)
        return sample[:self.sample_size]

    def run(self, data = 'normal', sample_size = None):
        self.sample_size = sample_size
        sample = self.generate_sample_distribution(data)
        
        mean_of_sample = np.mean(sample)
        sd_of_sample = np.std(sample)
        
        print(f'Sample Size: {len(sample)}')
        print(f'Population Size: {len(self.data)}')
        print(f'Mean of Sample: {mean_of_sample}')
        print(f'Mean of Population: {np.mean(self.data)}')
        print(f'S.D. of Sample: {sd_of_sample}')
        print(f'S.D. of Population: {np.std(self.data)}')
        
        plt.figure(figsize = (14,10))
        
        sns.distplot(self.data, label = 'Population')
        sns.distplot(sample, label = 'Sample')
        plt.legend()
        plt.show()