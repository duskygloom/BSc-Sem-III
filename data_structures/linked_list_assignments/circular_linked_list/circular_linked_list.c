#include <stdlib.h>
#include <stdio.h>

typedef struct Node {
    int value;
    struct Node *next;
} Node;

// creation and deletion

Node *create_list() {
    Node *list = malloc(sizeof(Node));
    list->value = 0;
    list->next = NULL;
    return list;
}

void delete_list(Node *list) {
    Node *head = list->next;
    Node *curr = head, *next = NULL;
    if (curr) {
        next = curr->next;
        free(curr);
        curr = next;
    }
    while (curr && curr != head) {
        next = curr->next;
        free(curr);
        curr = next;
    }
    free(list);
}

// traversal

void print_list(Node *list) {
    putchar('[');
    Node *head = list->next;
    Node *curr = list->next;
    if (curr) {
        printf("%d", curr->value);
        curr = curr->next;
    }
    while (curr && curr != head) {
        printf(", %d", curr->value);
        curr = curr->next;
    }
    if (curr) printf(" -> %d", curr->value);
    printf("]\n");
}

int count_list(Node *list) {
    int count = 0;
    Node *head = list->next;
    Node *curr = head;
    if (!curr) return 0;
    ++count;
    curr = curr->next;
    while (curr && curr != head) {
        ++count;
        curr = curr->next;
    }
    return count;
}

// insertion

void prepend(Node *list, int value) {
    Node *oldhead = list->next;
    Node *newhead = malloc(sizeof(Node));
    newhead->value = value;
    if (!oldhead) {
        newhead->next = newhead;
        list->next = newhead;
        return;
    }
    newhead->next = oldhead;
    list->next = newhead;
    Node *curr = oldhead;
    while (curr->next && curr->next != oldhead)
        curr = curr->next;
    curr->next = newhead;
}

void append(Node *list, int value) {
    Node *node = malloc(sizeof(Node));
    Node *head = list->next;
    node->value = value;
    if (!head) {
        node->next = node;
        list->next = node;
        return;
    }
    Node *curr = head;
    while (curr->next && curr->next != head) 
        curr = curr->next;
    curr->next = node;
    node->next = head;
}

void insert(Node *list, int index, int value) {
    Node *head = list->next;
    if (index == 0) {
        prepend(list, value);
        return;
    }
    else if (!head) return;
    Node *prev = head, *curr = head->next;
    int counter = 1;
    while (curr && curr != head && counter < index) {
        prev = curr;
        curr = curr->next;
        ++counter;
    }
    if (counter == index) {
        Node *node = malloc(sizeof(Node));
        node->value = value;
        node->next = prev->next;
        prev->next = node;
    }
}

// deletion

int pop_left(Node *list) {
    Node *oldhead = list->next;
    if (!oldhead) return 0;
    if (oldhead == oldhead->next) {
        int value = oldhead->value;
        free(oldhead);
        list->next = NULL;
        return value;
    }
    Node *newhead = oldhead->next;
    int value = oldhead->value;
    free(oldhead);
    list->next = newhead;
    Node *curr = newhead;
    while (curr->next && curr->next != oldhead) 
        curr = curr->next;
    curr->next = newhead;
    return value;
}

int pop_right(Node *list) {
    Node *head = list->next;
    if (!head) return 0;
    else if (head == head->next) {
        int value = head->value;
        free(head);
        list->next = NULL;
        return value;
    }
    Node *curr = head, *prev = list;
    while (curr->next && curr->next != head) {
        prev = curr;
        curr = curr->next;
    }
    int value = curr->value;
    free(curr);
    prev->next = head;
    return value;
}

int delete(Node *list, int index) {
    Node *head = list->next;
    if (index == 0) return pop_left(list);
    else if (!head) return 0;
    Node *prev = head, *curr = head->next;
    int counter = 1;
    while (curr && curr != head && counter < index) {
        prev = curr;
        curr = curr->next;
        ++counter;
    }
    if (counter == index) {
        int value = curr->value;
        Node *next = curr->next;
        free(curr);
        prev->next = next;
        return value;
    }
    return 0;
}

int *get_value_address(Node *list, int index) {
    Node *head = list->next;
    Node *curr = head;
    int counter = 0;
    while (curr && curr->next != head && counter < index) {
        curr = curr->next;
        ++counter;
    }
    if (counter == index) return &(curr->value);
    return NULL;
}

void ascending_sort(Node *list) {
    int *ith, *jth, temp;
    for (int i = 1; i < count_list(list); ++i)
        for (int j = i-1; j >= 0; --j) {
            ith = get_value_address(list, i);
            jth = get_value_address(list, j);
            if (*ith < *jth) {
                temp = *ith;
                *ith = *jth;
                *jth = temp;
                --i;
            }
        }
}

void descending_sort(Node *list) {
    int *ith, *jth, temp;
    for (int i = 1; i < count_list(list); ++i)
        for (int j = i-1; j >= 0; --j) {
            ith = get_value_address(list, i);
            jth = get_value_address(list, j);
            if (*ith > *jth) {
                temp = *ith;
                *ith = *jth;
                *jth = temp;
                --i;
            }
        }
}
