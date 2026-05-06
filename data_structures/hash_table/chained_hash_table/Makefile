CC		= gcc
BUILD	= build
OBJECTS	= $(BUILD)/hashtable.o $(BUILD)/linked_list.o $(BUILD)/table_item.o
BINARY	= a.exe

all: main

init:
	mkdir -p $(BUILD)

main: $(BUILD)/main.o $(OBJECTS)
	$(CC) -pg $^ -o $(BINARY)

test: $(BUILD)/test.o $(OBJECTS)
	$(CC) -pg $^ -o $(BINARY)

$(BUILD)/%.o: %.c
	$(CC) -pg $^ -o $@ -c

clean:
	rm $(BUILD)/*.o
