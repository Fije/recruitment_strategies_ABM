# -*- coding: utf-8 -*-
"""
Implements the various matplotlib plots for this project.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from model import Environment
from roles import Unassigned, Follower, Leader, Pheromone

def plot_p_fl(df):
    """
    Creates (and shows) the p vs (f + l) plot.

    Args:
        df: the dataframe containing 'pheromone', 'followers', and 'leaders'
    """
    plt.figure()
    plt.scatter(df['pheromone'], df['followers'] + df['leaders'])
    plt.xlabel(r'$p$')
    plt.ylabel(r'$f + l$')
    plt.show()

def plot_col(df, cols):
    """
    Plots the variables in the cols list.

    Args:
        df: the dataframe containing entries from cols
        cols: list containing the dict entries to be plotted.
    """
    plt.figure()
    df[cols].plot()
    plt.show()

def plot_continuous(env, steps=1000):
    """
    Shows the passed environment over time. Terminates gracefully when closing
    the animation window.

    Args:
        env: the environment to be shown
        steps (int): the amount of steps to animate (default 1000)
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim([0, env.width])
    ax.set_ylim([0, env.height])
    env.animate(ax)
    fig_num = plt.get_fignums()[0]

    for i in range(steps):
        if not plt.fignum_exists(fig_num): return False

        plt.title('iteration: ' + str(i))
        plt.pause(0.001)

        # Take a step
        env.step()

        # Store the state for animation
        env.animate(ax)
        fig.canvas.draw()
    return True
