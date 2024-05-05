def entity_data_values(soup, date):
    # Find all <td> tags within <tbody>
    td_tags = soup.find('tbody').find_all('td')

    # Group the <td> tags into lists for each entity
    entities_data = []
    entity_data = []

    for td in td_tags:
        text = td.get_text().strip()
        if td.a:
            # If the <td> contains an <a> tag, it's the start of a new entity
            if entity_data:
                entities_data.append(entity_data)
                entity_data = []  # Reset the entity_data list for the next entity
            entity_data.append(td.a.get_text())
        else:
            entity_data.append(text)

    # Append the last entity data
    if entity_data:
        entities_data.append(entity_data)
    # print(entities_data)
    print(f"{date}: Entities data is created...")
    return entities_data