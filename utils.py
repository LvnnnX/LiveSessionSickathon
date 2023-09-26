import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def visualize_type(df: pd.DataFrame) -> plt.Figure:
    """Visualisasi persebaran tipe dari dataframe Netflix"""
    x: pd.DataFrame = df.groupby('type')['type'].count()
    y: int = len(df)
    ratio = ((x / y).round(2))
    df_ratio = pd.DataFrame(ratio).T
    
    fig, ax = plt.subplots(1, 1, figsize=(6.5, 2.5))
    
    ax.barh(df_ratio.index, df_ratio['Movie'], color='#000082', label='Movie')
    ax.barh(df_ratio.index, df_ratio['TV Show'], left=df_ratio['Movie'], color='#800000', label='TV Show')
    
    ax.set_xticks([])
    ax.set_yticks([])
    
    for i in df_ratio.index:
        ax.annotate(f"{int(df_ratio['Movie'][i]*100)}%", xy=(df_ratio['Movie'][i]/2,i), va='center', ha='center', color='white', fontweight='bold', fontsize=30)
        ax.annotate(f"Movies", xy=(df_ratio['Movie'][i]/2,-0.15), va='center', ha='center', color='white', fontweight='bold', fontsize=10)
        
        ax.annotate(f"{int(df_ratio['TV Show'][i]*100)}%", xy=(df_ratio['Movie'][i]+df_ratio['TV Show'][i]/2,i), va='center', ha='center', color='white', fontweight='bold', fontsize=30)
        ax.annotate(f"Tv Show", xy=(df_ratio['Movie'][i]+df_ratio['TV Show'][i]/2,-0.15), va='center', ha='center', color='white', fontweight='bold', fontsize=10)
    
    return fig