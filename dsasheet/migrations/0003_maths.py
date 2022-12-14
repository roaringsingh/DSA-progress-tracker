# Generated by Django 4.1 on 2022-09-11 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("dsasheet", "0002_array_hql1_array_hql2_array_hql3_array_hql4_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Maths",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "meqs1",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "meqr1",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "meql1",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("meqnotes1", models.TextField(blank=True, null=True)),
                (
                    "meqs2",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "meqr2",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "meql2",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("meqnotes2", models.TextField(blank=True, null=True)),
                (
                    "meqs3",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "meqr3",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "meql3",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("meqnotes3", models.TextField(blank=True, null=True)),
                (
                    "meqs4",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "meqr4",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "meql4",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("meqnotes4", models.TextField(blank=True, null=True)),
                (
                    "meqs5",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "meqr5",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "meql5",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("meqnotes5", models.TextField(blank=True, null=True)),
                (
                    "meqs6",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "meqr6",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "meql6",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("meqnotes6", models.TextField(blank=True, null=True)),
                (
                    "meqs7",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "meqr7",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "meql7",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("meqnotes7", models.TextField(blank=True, null=True)),
                (
                    "meqs8",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "meqr8",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "meql8",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("meqnotes8", models.TextField(blank=True, null=True)),
                (
                    "meqs9",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "meqr9",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "meql9",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("meqnotes9", models.TextField(blank=True, null=True)),
                (
                    "mmqs1",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "mmqr1",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "mmql1",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("mmqnotes1", models.TextField(blank=True, null=True)),
                (
                    "mmqs2",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "mmqr2",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "mmql2",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("mmqnotes2", models.TextField(blank=True, null=True)),
                (
                    "mmqs3",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "mmqr3",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "mmql3",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("mmqnotes3", models.TextField(blank=True, null=True)),
                (
                    "mmqs4",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "mmqr4",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "mmql4",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("mmqnotes4", models.TextField(blank=True, null=True)),
                (
                    "mmqs5",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "mmqr5",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "mmql5",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("mmqnotes5", models.TextField(blank=True, null=True)),
                (
                    "mmqs6",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "mmqr6",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "mmql6",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("mmqnotes6", models.TextField(blank=True, null=True)),
                (
                    "mmqs7",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "mmqr7",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "mmql7",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("mmqnotes7", models.TextField(blank=True, null=True)),
                (
                    "mhqs1",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "mhqr1",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "mhql1",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("mhqnotes1", models.TextField(blank=True, null=True)),
                (
                    "mhqs2",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "mhqr2",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "mhql2",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("mhqnotes2", models.TextField(blank=True, null=True)),
                (
                    "mhqs3",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "mhqr3",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "mhql3",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("mhqnotes3", models.TextField(blank=True, null=True)),
                (
                    "mhqs4",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "mhqr4",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "mhql4",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("mhqnotes4", models.TextField(blank=True, null=True)),
                (
                    "gmqs1",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "gmqr1",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "gmql1",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("gmqnotes1", models.TextField(blank=True, null=True)),
                (
                    "gmqs2",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "gmqr2",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "gmql2",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("gmqnotes2", models.TextField(blank=True, null=True)),
                (
                    "gmqs3",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "gmqr3",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "gmql3",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("gmqnotes3", models.TextField(blank=True, null=True)),
                (
                    "gmqs4",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "gmqr4",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "gmql4",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("gmqnotes4", models.TextField(blank=True, null=True)),
                (
                    "gmqs5",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "gmqr5",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "gmql5",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("gmqnotes5", models.TextField(blank=True, null=True)),
                (
                    "gmqs6",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "gmqr6",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "gmql6",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("gmqnotes6", models.TextField(blank=True, null=True)),
                (
                    "gmqs7",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "gmqr7",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "gmql7",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("gmqnotes7", models.TextField(blank=True, null=True)),
                (
                    "gmqs8",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "gmqr8",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "gmql8",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("gmqnotes8", models.TextField(blank=True, null=True)),
                (
                    "ghqs1",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "ghqr1",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "ghql1",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("ghqnotes1", models.TextField(blank=True, null=True)),
                (
                    "ghqs2",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "ghqr2",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "ghql2",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("ghqnotes2", models.TextField(blank=True, null=True)),
                (
                    "ghqs3",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "ghqr3",
                    models.IntegerField(choices=[(1, "Yes"), (2, "No")], default=2),
                ),
                (
                    "ghql3",
                    models.IntegerField(
                        choices=[(1, "Python"), (2, "C++"), (3, "Java"), (4, "Other")],
                        default=4,
                    ),
                ),
                ("ghqnotes3", models.TextField(blank=True, null=True)),
                (
                    "uid",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
