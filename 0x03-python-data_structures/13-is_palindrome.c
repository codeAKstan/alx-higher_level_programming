#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - entry point
 * @head: the head of the list
 * Return: returns 1 if true or 0 if false
 */

int is_palindrome(listint_t **head)
{
	int len = 0;
	listint_t *current = *head;
	int i, j;
	int *elements;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (current != NULL)
	{
		len++;
		current = current->next;
	}

	elements = malloc(sizeof(int) * len);
	if (elements == NULL)
		return (0);

	current = *head;

	for (i = 0; i < len; i++)
	{
		elements[i] = current->n;
		current = current->next;
	}

	for (i = 0, j = len - 1; i < j; i++, j--)
	{
		if (elements[i] != elements[j])
		{
			free(elements);
			return (0);
		}
	}
	free(elements);
	return (1);
}
