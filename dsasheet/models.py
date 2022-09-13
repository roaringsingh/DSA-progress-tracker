from django import forms
from .model import *


# Create your models here.

class ArrayForm(forms.ModelForm):
    class Meta:
        model = arrays.Array
        fields = '__all__'
        widgets = {f'eqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 13)}
        temp = {f'mqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 27)}
        widgets.update(temp)
        temp = {f'hqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 6)}
        widgets.update(temp)


class MathsForm(forms.ModelForm):
    class Meta:
        model = maths.Maths
        fields = '__all__'
        widgets = {f'meqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 10)}
        temp = {f'mmqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 8)}
        widgets.update(temp)
        temp = {f'gmqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 9)}
        widgets.update(temp)
        temp = {f'mhqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 5)}
        widgets.update(temp)
        temp = {f'ghqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 4)}
        widgets.update(temp)


class StackForm(forms.ModelForm):
    class Meta:
        model = stacks.Stack
        fields = '__all__'
        widgets = {f'tqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 6)}
        temp = {f'swqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 5)}
        widgets.update(temp)
        temp = {f'seqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 6)}
        widgets.update(temp)
        temp = {f'smqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 8)}
        widgets.update(temp)


class HashForm(forms.ModelForm):
    class Meta:
        model = hash.Hash
        fields = '__all__'
        widgets = {f'heqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 3)}
        temp = {f'hmqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 3)}
        widgets.update(temp)
        temp = {f'beqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 5)}
        widgets.update(temp)
        temp = {f'bmqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 10)}
        widgets.update(temp)
        temp = {f'bhqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 6)}
        widgets.update(temp)


class StringForm(forms.ModelForm):
    class Meta:
        model = strings.String
        fields = '__all__'
        widgets = {f'eqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 6)}
        temp = {f'mqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 11)}
        widgets.update(temp)
        temp = {f'hqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 8)}
        widgets.update(temp)


class RecurForm(forms.ModelForm):
    class Meta:
        model = recursion.Recur
        fields = '__all__'
        widgets = {f'rqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 17)}
        temp = {f'bmqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 3)}
        widgets.update(temp)
        temp = {f'bhqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 5)}
        widgets.update(temp)
        temp = {f'dqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 8)}
        widgets.update(temp)


class LinkedForm(forms.ModelForm):
    class Meta:
        model = linklist.LinkedL
        fields = '__all__'
        widgets = {f'eqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 13)}
        temp = {f'mqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 14)}
        widgets.update(temp)
        temp = {f'hqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 3)}
        widgets.update(temp)


class TreeForm(forms.ModelForm):
    class Meta:
        model = trees.Tree
        fields = '__all__'
        widgets = {f'eqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 17)}
        temp = {f'mqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 19)}
        widgets.update(temp)
        temp = {f'hqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 8)}
        widgets.update(temp)


class HeapForm(forms.ModelForm):
    class Meta:
        model = heaps.Heap
        fields = '__all__'
        widgets = {f'mqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 9)}
        temp = {f'hqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 10)}
        widgets.update(temp)


class TravForm(forms.ModelForm):
    class Meta:
        model = traversal.Trav
        fields = '__all__'
        widgets = {f'bmqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 6)}
        temp = {f'bhqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 5)}
        widgets.update(temp)
        temp = {f'dmqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 10)}
        widgets.update(temp)
        temp = {f'dhqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 9)}
        widgets.update(temp)


class GraphForm(forms.ModelForm):
    class Meta:
        model = graphs.Graph
        fields = '__all__'
        widgets = {f'eqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 3)}
        temp = {f'mqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 15)}
        widgets.update(temp)


class DynamicForm(forms.ModelForm):
    class Meta:
        model = dynamic.DynamicP
        fields = '__all__'
        widgets = {f'eqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 5)}
        temp = {f'mqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 17)}
        widgets.update(temp)
        temp = {f'hqnotes{i}': forms.Textarea(attrs={"rows": 1, "cols": 30}) for i in range(1, 16)}
        widgets.update(temp)


class MiscForm(forms.ModelForm):
    class Meta:
        model = miscs.Misc
        fields = '__all__'
