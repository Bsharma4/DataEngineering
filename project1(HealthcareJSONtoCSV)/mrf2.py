import os, logging
import time
import click
import json
import pandas as pd
from transformations import *

__author__ = "Paul Boal"
__email__ = "boalpe@slu.edu"

#
#TODO: Here or in other .py files, you need to add your own code to parse the JSON files
#      This is a very simple function for parsing a much simpler JSON input file.
#      There are many ways I could do this, but I've decided to show it using basic
#      Python features rather than Pandas or another library because Pandads's support
#      for JSON won't be sufficient for our real files.
#
# This is a simple parser used for a much simpler test file
def parse_simple(inputfile, outputfile=None):
    """This function both writes to an output file and returns a dataframe
       with the information. That will make testing easier."""
    # Convert JSON to pandas dataframe
    # I know the data I'm looking for: name, type, breed
    # Other data I might encounter, I'll ignore.
    # Convert JSON to pandas dataframe
    
    df = pd.read_json(inputfile)

    # Flatten the nested in_network column
    in_network_df = pd.json_normalize(df['in_network'], record_path=['negotiated_rates', 'provider_groups'], 
                                    meta=[['name'], ['negotiation_arrangement'], ['billing_code'], 
                                            ['description'], ['billing_code_type'], ['billing_code_type_version']])

    # Merge the flattened in_network DataFrame with the main DataFrame
    merged_df = pd.merge(df.drop('in_network', axis=1), in_network_df, how='cross')

    # Save the merged data to a CSV file
    merged_df.to_csv(outputfile, index=False)

    return merged_df


@click.command()
@click.argument('filename', type=click.Path(exists=True, dir_okay=False))
@click.option('--loglevel', type=click.Choice(['ERROR','WARNING','INFO','DEBUG','NOTSET']), 
                            default='INFO', help='Set logging level')
def run(filename, loglevel):

    logger = logging.getLogger()
    logger.setLevel(loglevel)

    start_ts = time.perf_counter()
    logger.debug(f'Running in DEBUG')
    logger.info(f'Processing file: {filename}')

    #
    #TODO: Here, you need to call your functions to parse the JSON, 
    #      create the right output format, and write that to a CSV file
    #
    if filename[-5:] == '.json':
        outputfile = filename[:-5] + '.csv'
        df = parse_simple(filename,outputfile)

    runtime_sec = int(time.perf_counter() - start_ts)
    logger.info(f'Runtime: {runtime_sec} sec')

    return df



if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s():%(lineno)d - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    run()

