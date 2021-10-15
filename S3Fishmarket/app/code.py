import pandas as pd
import boto3
import pprint as p
import io

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

bucket_name = 'data-eng-resources'


def list_of_dataframes():
    fish_market_files = [
        pd.read_csv(s3_client.get_object(Bucket=bucket_name, Key='python/fish-market.csv')['Body']),
        pd.read_csv(s3_client.get_object(Bucket=bucket_name, Key='python/fish-market-mon.csv')['Body']),
        pd.read_csv(s3_client.get_object(Bucket=bucket_name, Key='python/fish-market-tues.csv')['Body'])
    ]
    return fish_market_files


combine_file = pd.concat(list_of_dataframes(), ignore_index=True)


# p.pprint(combine_file)

def names_of_species():
    list_of_species = []
    for species in combine_file["Species"]:
        if species not in list_of_species:
            list_of_species.append(species)
    return list_of_species


def avg_weight_for_species(species):
    weight = 0
    weight_count = 0
    for num in range(len(combine_file)):
        if combine_file["Species"][num] == species:
            weight_count += 1
            weight += combine_file["Weight"][num]
    avg_weight = weight / weight_count
    return avg_weight


def avg_length1_for_species(species):
    length1 = 0
    length1_count = 0
    for num in range(len(combine_file)):
        if combine_file["Species"][num] == species:
            length1_count += 1
            length1 += combine_file["Weight"][num]
    avg_length1 = length1 / length1_count
    return avg_length1


def avg_length2_for_species(species):
    length2 = 0
    length2_count = 0
    for num in range(len(combine_file)):
        if combine_file["Species"][num] == species:
            length2_count += 1
            length2 += combine_file["Weight"][num]
    avg_length2 = length2 / length2_count
    return avg_length2


def avg_length3_for_species(species):
    length3 = 0
    length3_count = 0
    for num in range(len(combine_file)):
        if combine_file["Species"][num] == species:
            length3_count += 1
            length3 += combine_file["Weight"][num]
    avg_length3 = length3 / length3_count
    return avg_length3


print(avg_length3_for_species("Whitefish"))


def avg_height_for_species(species):
    height = 0
    height_count = 0
    for num in range(len(combine_file)):
        if combine_file["Species"][num] == species:
            height_count += 1
            height += combine_file["Weight"][num]
    avg_height = height / height_count
    return avg_height


def avg_width_for_species(species):
    width = 0
    width_count = 0
    for num in range(len(combine_file)):
        if combine_file["Species"][num] == species:
            width_count += 1
            width += combine_file["Weight"][num]
    avg_width = width / width_count
    return avg_width


def weights_of_all_species():
    weights = []
    for species in names_of_species():
        weights.append(avg_weight_for_species(species))
    return weights


def length1_of_all_species():
    length1s = []
    for species in names_of_species():
        length1s.append(avg_length1_for_species(species))
    return length1s


def length2_of_all_species():
    length2s = []
    for species in names_of_species():
        length2s.append(avg_length2_for_species(species))
    return length2s


def length3_of_all_species():
    length3s = []
    for species in names_of_species():
        length3s.append(avg_length3_for_species(species))
    return length3s


def height_of_all_species():
    heights = []
    for species in names_of_species():
        heights.append(avg_height_for_species(species))
    return heights

# print(height_of_all_species())

def width_of_all_species():
    widths = []
    for species in names_of_species():
        widths.append(avg_width_for_species(species))
    return widths


# print(width_of_all_species())
def dict_of_data():
    data = {"Species": names_of_species(), "Weight": weights_of_all_species(), "Length1": length1_of_all_species(),
            "Length2": length2_of_all_species(), "Length3": length3_of_all_species(), "Height": height_of_all_species(),
            "Width": width_of_all_species()}
    return data

data = {"Species": names_of_species(), "Weight": weights_of_all_species(), "Length1": length1_of_all_species(),
            "Length2": length2_of_all_species(), "Length3": length3_of_all_species(), "Height": height_of_all_species(),
            "Width": width_of_all_species()}

# print(dict_of_data())
fish = pd.DataFrame(data)
str_buffer = io.StringIO()
fish.to_csv(str_buffer)
s3_client.put_object(Body=str_buffer.getvalue(), Bucket =bucket_name, Key="Data100/fish/sully.csv")

# def group_by_species():
#     averages = combine_file.groupby("Species").mean()
#     return averages
