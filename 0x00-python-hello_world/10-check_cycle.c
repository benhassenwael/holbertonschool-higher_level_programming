#include "lists.h"


/**
 * check_cycle - check if a singly linked list has a cycle in it
 * @list: pointer to a linked list to check
 *
 * Return: 0 if ther is no cycle and 1 if a cycle was found
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr, *jumper;

	if (!list || !list->next)
		return (0);
	ptr = list->next;
	jumper = ptr->next;
	while (jumper && jumper->next && ptr)
	{
		if (jumper == ptr)
			return (1);
		ptr = ptr->next;
		jumper = jumper->next->next;
	}
	return (0);
}
