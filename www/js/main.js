(function(){
window.App = {
    Models: {},
    Collections: {},
    Views: {}
};

window.template = function(id) {
    return _.template( $('#' + id).html() );
};


App.Models.Person = Backbone.Model.extend({
    defaults: {
        name: 'Guest User',
        age: 23,
        occupation: 'Worker',
    },
    validate: function(attrs, options){
        if (attrs.age < 0){
            return 'Age must be positive.';
        }
        if (!attrs.name){
            return 'Everyone must have a name.';
        }
    },
    work: function(){
        return this.get('name') + 'is working.';
    },
});


App.Collections.People = Backbone.Collection.extend({
    model: App.Models.Person,
});


App.Views.Person = Backbone.View.extend({
    tagName: 'li',
    // className: 'person',
    // id: 'person-id',

    template: template('personTemplate'),

    render: function(){
        this.$el.html( this.template(this.model.toJSON()));
        return this;
    },
});


App.Views.People = Backbone.View.extend({
    tagName: 'ul',
    render: function(){
        this.collection.each(function(person){
            var personView = new App.Views.Person({model: person});
            this.$el.append(personView.render().el);
        }, this);
        return this;
    }
});




var peopleCollection = new App.Collections.People([
    {
        name: 'Mohit Jain',
        age: 26
    },
    {
        name: 'Taroon Tyagi',
        age: 25,
        occupation: 'web designer'
    },
    {
        name: 'Rahul Narang',
        age: 26,
        occupation: 'Java Developer'
    }
]);


var peopleView = new App.Views.People({ collection: peopleCollection });
$(document.body).append(peopleView.render().el);
})();
