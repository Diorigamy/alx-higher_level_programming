#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: the singly linked list to scan through
 * Return: 0 if no cycle, 1 if there is cycle
 */
int check_cycle(listint_t *list)
{
  listint_t *begining = list, *end = list;
	int total = 0;
	
	while ((begining && end) && end->next)
	{
		begining = begining->next;
		if (end->next || end->next->next)
			end = end->next->next;
		else
			break;
		if (begining == end)
		{
			total = 1;
			break;
		}
	}
	return (total);
}
