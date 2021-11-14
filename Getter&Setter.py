# loop through and add getter and setters to output_list
def append_getters_and_setters_to_list(input_list, output_list):
    for value in input_list:
        output_list.append(f"public String get{value[0].capitalize()}{value[1:]}() " + "{\n"
                           + f"    return (String) this.attributes.get(\"{value}\");\n" + "}\n")
        output_list.append(f"public void set{value[0].capitalize()}{value[1:]}(String {value}) " + "{\n "
                           + f"    this.attributes.put(\"{value}\", {value});\n" + "}\n")


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    ldap_values = []
    final_output = []

    for line in lines:
        ldap_values.append(line.strip())

    append_getters_and_setters_to_list(ldap_values, final_output)

    for output in final_output:
        print(output)