#include <stdlib.h>
#include "lists.h"

/**
* insert_node - inserts a node into a sorted singly linked list
* @head: a pointer to a pointer to head
* @number: an integer
*
* Return: the address of the new node or NULL on failure
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = NULL;

	if (!head)
		return (NULL);
	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = number;
	while (*head && (*head)->n < number)
		head = &((*head)->next);
	node->next = *head;
	*head = node;
	return (node);
}
