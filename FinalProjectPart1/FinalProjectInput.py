# Kimberly Jin
# 2053517

import csv
import datetime


class Inventory:
    def __init__(self, item_id="", manufacturer="", type="", price="", date="", damaged=""):
        self.item_id = item_id
        self.manufacturer = manufacturer
        self.type = type
        self.price = price
        self.date = date
        self.damaged = damaged


# sort with manufacturer name
def sort_by_manufacturer(inventoryItem):
    return inventoryItem.manufacturer


def sort_by_type(my_item):
    return my_item.type

# for sorting by item id


def sort_by_item_id(my_item):
    return my_item.item_id


def sort_by_service_date(item):
    return item.date


def sort_by_item_price(my_item):
    return my_item.price


def sort_by_year(item):
    year_index = len(item.date)
    return item.date[year_index-5:]


def sort_by_month(item):
    month_index = item.date.find('/')
    slash = item.date.find('/', month_index+1)
    return item.date[month_index+1:slash]


def sort_by_day(item):
    month_index = item.date.find('/')
    return item.date[0:month_index]


if __name__ == '__main__':
    # input files
    file_manufacturer_list = "ManufacturerList.csv"
    file_price_list = "PriceList.csv"
    file_service_date_list = "ServiceDatesList.csv"

    today = datetime.date.today()
    items_dict = {}

    # reading manufacturer's list
    with open(file_manufacturer_list, 'r') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',')
        line_num = 0  # this is here *existing*
        # reads each line in the file
        for information in file_reader:
            size_of_line = len(information)
            itemid = information[0]

            # nested dictionary
            items_dict[itemid] = {}
            itemmanu = information[1]
            itemtype = information[2]

            # update dict
            if size_of_line == 4:
                itemdamage = information[3]
                items_dict[itemid]['item_id'] = itemid
                items_dict[itemid]['manufacturer'] = itemmanu
                items_dict[itemid]['type'] = itemtype
                items_dict[itemid]['damaged'] = itemdamage
            else:
                # copy paste lol
                items_dict[itemid]['item_id'] = itemid
                items_dict[itemid]['manufacturer'] = itemmanu
                items_dict[itemid]['type'] = itemtype
                items_dict[itemid]['damaged'] = ""

    # inventory fully created - read through all the files
    # opening price list
    # add prices - match with item id
    with open(file_price_list, 'r') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',')
        line_num = 0
        # reads each line in the file
        for information in file_reader:
            # add price to item dict id
            itemid = information[0]
            itemprice = information[1]
            items_dict[itemid]['price'] = itemprice

    # opening service dates list
    # add service date - match with item id
    with open(file_service_date_list, 'r') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',')
        line_num = 0
        # reads each line in the file
        for information in file_reader:
            # add service date to item dict id
            itemid = information[0]
            item_service_date = information[1]
            items_dict[itemid]['date'] = item_service_date
            # my_manu_list[line_num] = item.Inventory(item_id=itemid, name=itemname, type=itemtype)
            # for individual in information:
    # fullInventory = InventoryReports(items_dict)

    my_item_list = []
# self, item_id="", manufacturer="", type="", damaged=""):
    # to sort my manufacturer name, convert to list and use sort method
    for item in items_dict.values():
        my_item_list.append(Inventory(item_id=item['item_id'],
                                      manufacturer=item['manufacturer'],
                                      type=item['type'],
                                      price=item['price'],
                                      date=item['date'],
                                      damaged=item['damaged']))
    my_item_list.sort(key=sort_by_type)
    my_item_list.sort(key=sort_by_manufacturer)
    # works

    # open full inventory csv, need to write so 'w'
    # next, write each inventory list to full inventory
    with open("FullInventory.csv", 'w', newline="") as csvfile:
        fullInventory = csv.writer(csvfile, delimiter=',')

        for inventoryItem in my_item_list:
            fullInventory.writerow([inventoryItem.item_id, inventoryItem.manufacturer, inventoryItem.type,
                                   inventoryItem.price, inventoryItem.date, inventoryItem.damaged])

    # do item type inventory list

    # item ID, manufacturer, price, service date, if damaged, SORT BY ITEM ID

    # create a list for each item type
    my_item_type_list = []

    # create a csv file for each type of item

    with open(file_manufacturer_list, 'r') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',')
        line_num = 0  # this is here *existing*
        # reads each line in the file
        for information in file_reader:
            itemtype = information[2]
            my_item_type_list.append(itemtype)

    my_temp_item_list = []
    for item_type in my_item_type_list:
        # type is the type of items in the list
        # don't forget to clear list at the end of the for loop
        for my_item in my_item_list:
            # my_item each inventory item in the list previously created
            if my_item.type == item_type:
                my_temp_item_list.append(my_item)
        # for loop added all the items of the same type into the list

        # sort items by id

        my_temp_item_list.sort(key=sort_by_item_id)

        # after adding the same type, add to item's file

        item_type_file = item_type + "Inventory.csv"
        with open(item_type_file, 'w', newline="") as csvfile:
            write_to_file = csv.writer(csvfile, delimiter=',')
            for items in my_temp_item_list:
                temp_write_list = [items.item_id, items.manufacturer, items.price, items.date, items.damaged]
                write_to_file.writerow(temp_write_list)
        # end of for loop
        # clear temp list
        my_temp_item_list.clear()
        # repeat for all the other item types
    # works

    # finished adding items by list to csv

    # commencing past service date inventory csv
    # row should contain: item ID, manufacturer name, item type, price, service date, and list if it is damaged
    # order of service date from oldest to most recent
    my_service_list = []

    # get today's date, then set the month day and year

    for item_past_date in my_item_list:
        # this is calling today's date
        today = datetime.date.today()
        today_year = int(today.year)
        today_month = int(today.month)
        today_day = int(today.day)

        # this is the service date
        current_item_date = item_past_date.date
        current_item_date_list = current_item_date.split('/')

        current_item_month = int(current_item_date_list[0])
        current_item_day = int(current_item_date_list[1])
        current_item_year = int(current_item_date_list[2])

        if today_year > current_item_year:
            # if today's date, the year is greater than service date year, add to list
            my_service_list.append(item_past_date)
            # print("hello ", current_item_year)
        elif today_year == current_item_year:
            if today_month > current_item_month:
                my_service_list.append(item_past_date)
                # print("here ", current_item_month)
            elif today_month == current_item_month:
                if today_day > current_item_day:
                    # print("stupid ", item_past_date)
                    my_service_list.append(item_past_date)
        # finished adding all the items with service dates before today's date

    # time to sort service date list
    my_service_list.sort(key=sort_by_service_date, reverse=True)
    # print(my_service_list[1].date)

    pure_list_of_dates = []
    for my_item in my_service_list:
        pure_list_of_dates.append(my_item.date)
    pure_list_of_dates.sort()
    my_sorted_list = sorted([datetime.datetime.strptime(date, '%m/%d/%Y') for date in pure_list_of_dates])
    [item.strftime('%m/%d/%Y') for item in my_sorted_list]
    # print(my_sorted_list)
    new_service_list = []

    # attempt to sort
    for my_item in my_service_list:
        date_list = my_item.date.split('/')
        for date in pure_list_of_dates:
            date_list_2 = date.split('/')
            # sort by year, it it's less
            if int(date_list[2]) < int(date_list_2[2]):
                new_service_list.append(my_item)
                # print('first')
            # sort by month it same year
            elif int(date_list[2]) == int(date_list_2[2]):
                if int(date_list[0]) < int(date_list_2[0]):
                    new_service_list.append(my_item)
                    # print('second')
                # sort by day if same month
                elif int(date_list[0]) == int(date_list_2[0]):
                    if int(date_list[1]) < int(date_list_2[1]):
                        new_service_list.append(my_item)
                        # print('third')
            else:
                new_service_list.append(my_item)
        if my_item in new_service_list:
            if new_service_list.count(my_item) > 1:
                new_service_list.remove(my_item)
            else:
                continue
        else:
            new_service_list.append(my_item)

    new_service_list.sort(key=sort_by_month)
    # new_service_list.sort(key=sort_by_day)
    new_service_list.sort(key=sort_by_year)

    # print(new_service_list[0].date, new_service_list[1].date, new_service_list[2].date)
    # works now ... i think

    with open('PastServiceDateInventory.csv', 'w', newline="") as csvfile:
        file_write = csv.writer(csvfile, delimiter=',')
        for my_item in new_service_list:
            if my_item.damaged == '':
                temp_write_list = [my_item.item_id, my_item.manufacturer, my_item.type,
                                   my_item.price, my_item.date]
            else:
                temp_write_list = [my_item.item_id, my_item.manufacturer, my_item.type,
                                   my_item.price, my_item.date, my_item.damaged]
            file_write.writerow(temp_write_list)

    # starting damaged inventory csv file
    # Each row should contain : item ID, manufacturer name, item type, price, and service date
    # items must appear in the order of most expensive to least expensive

    my_list_of_damaged_items = []

    for my_item in my_item_list:
        if my_item.damaged != '':
            my_list_of_damaged_items.append(my_item)

    # sort the list of damaged items by price

    my_list_of_damaged_items.sort(key=sort_by_item_price, reverse=True)

    # reverse is true cause want to sort by highest price to smallest price

    # add list to csv file

    with open('DamagedInventory.csv', 'w', newline="") as csvfile:
        write_file = csv.writer(csvfile, delimiter=',')
        for my_item in my_list_of_damaged_items:
            # make a list in the order

            temp_write_list = [my_item.item_id, my_item.manufacturer, my_item.type,
                               my_item.price, my_item.date]
            write_file.writerow(temp_write_list)
