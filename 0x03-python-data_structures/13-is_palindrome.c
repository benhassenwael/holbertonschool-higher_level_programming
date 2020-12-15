#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 *
 * Return: 1 if the list is palindrome and 0 if it is not
 */
int is_palindrome(listint_t **head)
{
	listint_t *looper, *mid, *top;
	unsigned int prev_distance, i = 0;

	if (!head || !(*head) || !((*head)->next))
		return (1);
	if (!((*head)->next)->next)
		return ((*head)->n == ((*head)->next)->n);
	looper = mid = *head;
	while (looper && looper->next)
	{
		mid = mid->next;
		looper = (looper->next)->next;
		i++;
	}
	if (!(mid->next)->next)
		return ((*head)->n == (mid->next)->n);
	top = *head;
	while (top != mid)
	{
		looper = mid;
		prev_distance = i;
		for (i = 0; i < prev_distance - 1; i++)
			looper = looper->next;
		if (top->n != looper->n)
			return (0);
		top = top->next;
	}
	return (1);
}
