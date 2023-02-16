import pandas as pd
import datetime as dt
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

def eplus_to_datetime(date_str):
	if date_str[-8:-6] != '24':
		dt_obj = pd.to_datetime(date_str)
	else:
		date_str = date_str[0:-8] + '00' + date_str[-6:]
		dt_obj = pd.to_datetime(date_str) + dt.timedelta(days=1)
	return dt_obj

def plot_1D_results(output_paths, plot_column_name,
					y_axis_title, plot_title):
	fig, ax = plt.subplots(1, 1, figsize=(20,10))
	fontsize = 20
	for item in output_paths.keys():
		this_path = output_paths[item]
		this_df = pd.read_csv(this_path)
		this_df['Date/Time'] = '2002' + this_df['Date/Time']
		this_df['Date/Time'] = this_df['Date/Time'].apply(eplus_to_datetime)
		data_st_date = this_df.iloc[0]['Date/Time']
		data_ed_date = this_df.iloc[-1]['Date/Time']
		date_list = this_df['Date/Time']
		this_y = this_df[plot_column_name].values
		ax.plot(date_list, this_y,
				alpha = 0.7,
				linestyle = '--',
				linewidth = 2,
				label = item)
		datetime_ax_loc = mdates.HourLocator()
		datetime_ax_fmt = mdates.DateFormatter('%H:%M')
		ax.xaxis.set_major_locator(datetime_ax_loc)
		ax.xaxis.set_major_formatter(datetime_ax_fmt)
		for tick in ax.xaxis.get_major_ticks():
			tick.label.set_fontsize(fontsize*0.8)
		for tick in ax.yaxis.get_major_ticks():
			tick.label.set_fontsize(fontsize*0.8)
		ax.tick_params('x', labelrotation=45)
		ax.set_xlabel('Time(%s to %s)'%(data_st_date, data_ed_date),
				fontsize = fontsize)
		ax.set_ylabel(y_axis_title,
				fontsize = fontsize)
		ax.set_title(plot_title,
				fontsize = fontsize)
		ax.legend(fontsize = fontsize)		
		plt.savefig('./param_exp_1_plot.png')
