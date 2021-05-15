import numpy as np

def calculate(list):
    if len(list)!=9:
        raise ValueError('List must contain nine numbers.')
    else:
        a = np.array(list).reshape(3,3)
        dic = {}
        dic['mean'] = [np.mean(a,axis=0).tolist(),np.mean(a,axis=1).tolist(),np.mean(a)]
        dic['variance'] = [np.var(a,axis=0).tolist(),np.var(a,axis=1).tolist(),np.var(a)]
        dic['standard deviation'] = [np.std(a,axis=0).tolist(),np.std(a,axis=1).tolist(),np.std(a)]
        dic['max'] = [np.amax(a,axis=0).tolist(),np.amax(a,axis=1).tolist(),np.amax(a)]
        dic['min'] = [np.amin(a,axis=0).tolist(),np.amin(a,axis=1).tolist(),np.amin(a)]
        dic['sum'] = [np.sum(a,axis=0).tolist(),np.sum(a,axis=1).tolist(),np.sum(a)]
        return dic