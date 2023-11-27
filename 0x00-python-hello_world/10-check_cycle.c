#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/**
 * check_cycle - entry point
 * @list: the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tortise, *hare;

	if (!list)
		return (0);

	tortise = list;
	hare = list->next;

	while (hare && tortise && hare->next)
	{
		if (tortise == hare)
			return (1);
		tortise = tortise->next;
		hare = hare->next->next;
	}
	return (0);
}
