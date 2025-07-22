import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from datetime import date
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter, MaxNLocator
from .cleaning import get_last_day_each_quarter
from .calcs import to_percent, to_ratio
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm
from matplotlib.colors import to_rgba


'''
All plotting functions are located here including the plotting of the basic subplot, labeling the points, and building the table
The basic subplot is built without any axis information, and the edge of the plot is based on the min and max values
The point labels are added to each point on the line, and can be adjusted with their location/xycords
The table builder adds a table given information from a df and the location can be adjusted based on the needs for the graph
'''

#### Line Graphs ####

# Allows for building simple line graphs on a specified subplot range
def plot_basic_lines(index_list, prepared_dataframes, column, row, subplt_row, subplot_col, figsize, quarterly=None, start_value=None, end_value=None):
    # Sets up the subplot and axes for use
    fig, axes_array = plt.subplots(subplt_row, subplot_col, figsize=figsize, constrained_layout=True)

    # Flattens the axes so we can acess like an array
    if isinstance(axes_array, np.ndarray):
        axes = axes_array.flatten()
    else:
        axes = [axes_array]

    dfs = []

    # Builds each subplot using the prepped dfs
    for i, index in enumerate(index_list):
        ax = axes[i]
        if (quarterly == True):
            df = get_last_day_each_quarter(prepared_dataframes[index], start_value, end_value)
            dfs.append(df)
        else:
            df = prepared_dataframes[index]
            dfs.append(df)

        ax.plot(df[row], df[column])

    # Turn off unused axes
    for i in range(len(index_list), subplt_row * subplot_col):
        axes[i].axis('off')

    return fig, axes, dfs

# Allows for building colored line graphs on a specified subplot range
def plot_colored_lines(index_list, colors, prepared_dataframes, column, row, subplt_row, subplot_col, figsize, quarterly=None, start_value=None, end_value=None):
    fig, axes_array = plt.subplots(subplt_row, subplot_col, figsize=figsize, constrained_layout=True)

    if isinstance(axes_array, np.ndarray):
        axes = axes_array.flatten()
    else:
        axes = [axes_array]

    dfs = []

    # Zips together the index_list and colors so they can be used in tandem when plotting
    for i, (index, color) in enumerate(zip(index_list, colors)):
        ax = axes[i]
        if (quarterly == True):
            df = get_last_day_each_quarter(prepared_dataframes[index], start_value, end_value)
            dfs.append(df)
        else:
            df = prepared_dataframes[index]
            dfs.append(df)

        ax.plot(df[row], df[column], color=color)

    # Turn off unused axes
    for i in range(len(index_list), subplt_row * subplot_col):
        axes[i].axis('off')

    return fig, axes, dfs

# Allows for building line graphs with a colored point on the lines on a specified subplot range
def plot_scatter_lines(index_list, colors, prepared_dataframes, column, row, subplt_row, subplot_col, figsize, mark, quarterly=None, start_value=None, end_value=None):
    fig, axes_array = plt.subplots(subplt_row, subplot_col, figsize=figsize, constrained_layout=True)

    if isinstance(axes_array, np.ndarray):
        axes = axes_array.flatten()
    else:
        axes = [axes_array]

    dfs = []

    for i, (index, color) in enumerate(zip(index_list, colors)):
        ax = axes[i]
        if (quarterly == True):
            df = get_last_day_each_quarter(prepared_dataframes[index], start_value, end_value)
            dfs.append(df)
        else:
            df = prepared_dataframes[index]
            dfs.append(df)

        ax.plot(df[row], df[column], marker=mark, color='black', markerfacecolor=color)

    # Turn off unused axes
    for i in range(len(index_list), subplt_row * subplot_col):
        axes[i].axis('off')

    return fig, axes, dfs

#### Scatterplots ####

# Allows for building simple scatterplot on a specified subplot range
def plot_basic_scatter(index_list, prepared_dataframes, column, row, subplt_row, subplot_col, figsize, quarterly=None, start_value=None, end_value=None):
    # Sets up the subplot and axes for use
    fig, axes_array = plt.subplots(subplt_row, subplot_col, figsize=figsize, constrained_layout=True)

    # Flattens the axes so we can acess like an array
    if isinstance(axes_array, np.ndarray):
        axes = axes_array.flatten()
    else:
        axes = [axes_array]

    dfs = []

    # Builds each subplot using the prepped dfs
    for i, index in enumerate(index_list):
        ax = axes[i]
        # Allows for specification of how many points wanted on subplot
        if (quarterly == True):
            df = get_last_day_each_quarter(prepared_dataframes[index], start_value, end_value)
            dfs.append(df)
        else:
            df = prepared_dataframes[index]
            dfs.append(df)

        ax.scatter(df[row], df[column])

    # Turn off unused axes
    for i in range(len(index_list), subplt_row * subplot_col):
        axes[i].axis('off')

    return fig, axes, dfs

# Allows for building colored scatterplots on a specified subplot range
def plot_colored_scatter(index_list, colors, prepared_dataframes, column, row, subplt_row, subplot_col, figsize, quarterly=None, start_value=None, end_value=None):
    fig, axes_array = plt.subplots(subplt_row, subplot_col, figsize=figsize, constrained_layout=True)

    if isinstance(axes_array, np.ndarray):
        axes = axes_array.flatten()
    else:
        axes = [axes_array]

    dfs = []

    # Zips together the index_list and colors so they can be used in tandem when plotting
    for i, (index, color) in enumerate(zip(index_list, colors)):
        ax = axes[i]
        if (quarterly == True):
            df = get_last_day_each_quarter(prepared_dataframes[index], start_value, end_value)
            dfs.append(df)
        else:
            df = prepared_dataframes[index]
            dfs.append(df)
        
        ax.scatter(df[row], df[column], color=color)


    # Turn off unused axes
    for i in range(len(index_list), subplt_row * subplot_col):
        axes[i].axis('off')

    return fig, axes, dfs

#### Tables ####

# Builds a table on a specified ax
def table_builder(df_table, ax, location):
    table = ax.table(cellText=df_table.values, 
                             colLabels=df_table.columns, 
                             loc=location, cellLoc='center')
    # Specific font selections so all the tables are identical in looks
    table.auto_set_font_size(False)
    table.set_fontsize(7)
    table.scale(.12, 1.2)

custom_cmap = LinearSegmentedColormap.from_list(
    'red_white_green',
    [(0, '#E50000'), (0.5, 'white'), (1.0, '#15B10A')]
)

# Plots a styled table with colored boxes
def plot_styled_table(raw_df, display_df, ax, width_scale, cmap=None, center=0, fontsize=4, loc='center'):
    # Creates a list of the formatted data and count num of rows/cols
    cell_text = [list(row) for row in display_df.itertuples(index=False)]
    nrows, ncols = len(cell_text) + 1, len(display_df.columns)

    # Sets up specific widths for the col
    col_widths = ([0.1] * ncols) * width_scale

    # Creates the table
    table = ax.table(
        cellText=cell_text,
        colLabels=display_df.columns, colWidths=col_widths,
        loc='center', cellLoc='left'
    )

    # Table sizing is adjusted
    table.auto_set_font_size(False)
    table.set_fontsize(fontsize)
    table.scale(1.0, 0.6)

    # Sets up the color
    cmap_func = custom_cmap if cmap is None else plt.colormaps[cmap]

    # Selects on the cols that we want to apply the heatmap to
    delta_col_indices = [
        idx for idx, col in enumerate(raw_df.columns)
        if 'Δ' in str(col)
    ]

    if delta_col_indices:
        # Iterates through the values and checks to make sure they are numbers
        data_vals = raw_df.iloc[:, delta_col_indices].apply(
            pd.to_numeric, errors='coerce').to_numpy().flatten()
        data_vals = data_vals[~np.isnan(data_vals)]

        if len(data_vals) > 0:
            # Sets the min and the max associated with the colors
            vmin, vmax = np.min(data_vals), np.max(data_vals)
            norm = TwoSlopeNorm(vmin=vmin, vcenter=center, vmax=vmax)

            # Loops over the rows 
            for i in range(raw_df.shape[0]):
                # Loops over the specified column
                for j in delta_col_indices:
                    try:
                        # Removes the formatting and turns to a float
                        val_str = str(raw_df.iat[i, j]).replace('bps', '').replace('%', '').strip()
                        val = float(val_str)

                        # Associates a color with the value and changes the background
                        color = cmap_func(norm(val))
                        rgba = to_rgba(color, alpha=0.7)
                        cell = table[(i + 1, j)]
                        cell.set_facecolor(rgba)
                    except:
                        continue


    # Auto adjusts the first columns width to ensure there is no overlapping
    for col_idx in range(1):
        table.auto_set_column_width(col_idx)

    # Iterates through the rows and columns getting the info about each cell
    for (row, col), cell in table.get_celld().items():
        # Formats based on the specified if statements
        if row == 0:
            cell.set_linewidth(1) 
        elif col == 0 and row == 0:
            cell.set_linewidth(1)
        elif col == 0:
            cell.visible_edges = 'LR'
            cell.set_linewidth(1)
        else:
            cell.set_linewidth(0)

        if row == 0:
            cell.set_text_props(weight='bold')

        if col == 0:
            cell.get_text().set_ha('left')
            cell.PAD = 0.03
            if row != 0:
                cell.get_text().set_weight('bold')
        else:
            cell.get_text().set_ha('center')

    # Hides axis to look good on subplot
    ax.axis('off')

# The same idea/format as above except for a few parts that are commented below
def plot_styled_table_stacked(raw_df, display_df, ax, width_scale, cmap=None, center=0, fontsize=4, loc='center'):
    # Need to split the headers since we have stacked ones here
    top_headers = [col[0] for col in display_df.columns]
    bottom_headers = [col[1] for col in display_df.columns]

    cell_text = [top_headers, bottom_headers] + [list(row) for row in display_df.itertuples(index=False)]
    nrows, ncols = len(cell_text), len(display_df.columns)

    col_widths = ([0.1] * ncols) * width_scale

    table = ax.table(cellText=cell_text,
                     colLabels=None,
                     colWidths=col_widths, loc=loc, cellLoc='left')

    table.auto_set_font_size(False)
    table.set_fontsize(fontsize)
    table.scale(1.0, 0.6)


    if cmap is None:
        cmap_func = custom_cmap
    else:
        cmap_func = plt.colormaps[cmap]

    # Selects the specific column we want highlighted
    delta_col_indices = [
        idx for idx, col in enumerate(raw_df.columns)
        if isinstance(col, tuple) and col[1] == 'Net Δ'
    ]

    if delta_col_indices:
        data_vals = raw_df.iloc[:, delta_col_indices].apply(
            pd.to_numeric, errors='coerce').to_numpy().flatten()
        data_vals = data_vals[~np.isnan(data_vals)]

        if len(data_vals) > 0:
            vmin, vmax = np.min(data_vals), np.max(data_vals)
            norm = TwoSlopeNorm(vmin=vmin, vcenter=center, vmax=vmax)

            for i in range(raw_df.shape[0]):
                for j in delta_col_indices:
                    try:
                        val_str = str(raw_df.iat[i, j]).replace('bps', '').replace('%', '').strip()
                        val = float(val_str)
                        normed_val = norm(val)
                        color = cmap_func(normed_val)
                        rgba = to_rgba(color, alpha=0.7)

                        # Need to be index plus 2 to skip over the stacked headers
                        cell = table[(i + 2, j)]
                        cell.set_facecolor(rgba)
                    except:
                        continue

    table.auto_set_font_size(False)
    table.set_fontsize(fontsize)
    ax.axis('off')
    

    for col_idx in range(1):
        table.auto_set_column_width(col_idx)

    for (row, col), cell in table.get_celld().items():
        cell.set_fontsize(3)
            
        if row == 0:
            cell.visible_edges = 'LRT'
            cell.set_linewidth(1) 
            cell.set_text_props(weight='bold')
        elif row == 1:
            cell.visible_edges = 'LRB'
            cell.set_linewidth(1) 
            cell.set_text_props(weight='bold')
        else:
            cell.set_linewidth(0)
              

        if col == 0:
            cell.get_text().set_ha('left')
            cell.PAD = 0.03
            cell.visible_edges = 'LR'
            cell.set_linewidth(1)
            cell.get_text().set_weight('bold')
        else:
            cell.get_text().set_ha('center')

        if col == 0 and row == 0:
            cell.set_linewidth(1)
            cell.set_text_props(weight='bold')
            cell.visible_edges = 'LRT'
        if col == 0 and row == 1:
            cell.set_linewidth(1)
            cell.set_text_props(weight='bold')
            cell.visible_edges = 'LRB'
            
    ax.axis('off')

#### Styling axes ####

# Works for building a plot with just the basic x and y axis from the plotting
def simple_axes(ax, title):
    ax.set_title(title, fontweight='bold')


# Works for building a plot with just a title and nothing else
def style_axes_blank(ax, title):
    ax.set_title(title, fontweight='bold')
    ax.set_ylabel(' ')
    ax.set_xlabel(' ')
    ax.set_xticks([])
    ax.set_yticks([])

# Works for styling with a date on x-axis and allows either (% or x) formatting on y-axis
def style_axes_date(ax, df, title, ending, dateperiods, format):
    ax.set_title(title, fontweight='heavy', style='italic')

    ax.tick_params(labelsize=12)
    ax.set_ylabel('')

    # Allows for easy formatting of percent or ratio on y-axis
    if ending == 'percent':
        ax.yaxis.set_major_formatter(FuncFormatter(to_percent))
    elif ending == 'ratio':
        ax.yaxis.set_major_formatter(FuncFormatter(to_ratio))

    ax.yaxis.set_major_locator(MaxNLocator(nbins=4, prune=None))

    start_date = df['date'].iloc[0]
    end_date = df['date'].iloc[-1]

    # Allows for selection of the time period shown on x-axis, along with formatting
    tick_dates = pd.date_range(start=start_date, end=end_date, periods=dateperiods)
    ax.set_xticks(tick_dates)
    ax.xaxis.set_major_formatter(mdates.DateFormatter(format))

#### Annotating Values ####

# Works for labeling a single or many points on a specified subplot
def point_label(indices, df, ax, location, xcord, ycord, value1=None, row=None, value2=None):
    # Looks to see if the indices given are an int
    if isinstance(indices, int):
        # If True, then it creates a range from zero to the int
        indices = [indices]
    # If False, then it goes straight to this for loop
    for i in indices:
        # If no values are given nothing happens
        if value1 is None and value2 is None:
            break

        # If one value is given to annotate then also need to specify row value, so annotation can be placed correctly
        elif value1 is not None and value2 is None:
            y = df[value1].iloc[i]
            x = df[row].iloc[i]

            label = f'{y:.2f}'
            ax.annotate(label, (x, y), textcoords="offset points", xytext=(xcord, ycord),
                    ha=location, fontsize=7)

        # If both values are given then annotation is shown    
        else:
            y = df[value1].iloc[i]
            x = df[value2].iloc[i]

            label = f"   {y:.2f} \n {x}"
            ax.annotate(label, (x, y), textcoords="offset points", xytext=(xcord, ycord),
                        ha=location, fontsize=7)
